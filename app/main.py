from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.auth import get_password_hash
from app.database import Base, SessionLocal, engine
from app.models import ceu, curso, atividade, admin
from app.models.admin import Admin
from app.routes.ceu_routes import router as ceu_router
from app.routes.curso_routes import router as curso_router
from app.routes.atividade_routes import router as atividade_router
from app.routes.auth_routes import router as auth_router

app = FastAPI(title="Projeto Integrador API", version="1.0")

# Configurar CORS para aceitar requisições do front-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especificar domínios: ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(ceu_router)
app.include_router(curso_router)
app.include_router(atividade_router)
Base.metadata.create_all(bind=engine)


def create_default_admin() -> None:
    db = SessionLocal()
    try:
        if not db.query(Admin).first():
            db.add(
                Admin(
                    email="admin.pi@gmail.com",
                    senha_hash=get_password_hash("admin"),
                )
            )
            db.commit()
    finally:
        db.close()


create_default_admin()


@app.get("/", response_model=dict)
def root() -> dict[str, str]:
    """Retorna um status simples da API."""
    return {"msg": "API funcionando"}
