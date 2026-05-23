import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database import Base
from app.routes.ceu_routes import get_db as get_ceu_db
from app.routes.curso_routes import get_db as get_curso_db
from app.routes.atividade_routes import get_db as get_atividade_db
from app.routes.auth_routes import get_db as get_auth_db

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="session")
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def db_session(setup_database):
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture()
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_ceu_db] = override_get_db
    app.dependency_overrides[get_curso_db] = override_get_db
    app.dependency_overrides[get_atividade_db] = override_get_db
    app.dependency_overrides[get_auth_db] = override_get_db
    # Also override get_db in auth.py if it's imported correctly
    from app.auth import get_db as auth_get_db

    app.dependency_overrides[auth_get_db] = override_get_db

    with TestClient(app) as c:
        yield c

    app.dependency_overrides.clear()


@pytest.fixture()
def admin_token(client, db_session):
    from app.models.admin import Admin
    from app.auth import get_password_hash

    admin = Admin(email="admin@test.com", senha_hash=get_password_hash("testpassword"))
    db_session.add(admin)
    db_session.commit()

    response = client.post(
        "/login",
        data={"username": "admin@test.com", "password": "testpassword"},
    )
    return response.json()["access_token"]
