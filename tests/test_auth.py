def test_login_success(client, db_session):
    from app.models.admin import Admin
    from app.auth import get_password_hash

    admin = Admin(
        email="testadmin@test.com", senha_hash=get_password_hash("password123")
    )
    db_session.add(admin)
    db_session.commit()

    response = client.post(
        "/login",
        data={"username": "testadmin@test.com", "password": "password123"},
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_login_invalid_password(client, db_session):
    from app.models.admin import Admin
    from app.auth import get_password_hash

    admin = Admin(
        email="testadmin@test.com", senha_hash=get_password_hash("password123")
    )
    db_session.add(admin)
    db_session.commit()

    response = client.post(
        "/login",
        data={"username": "testadmin@test.com", "password": "wrongpassword"},
    )
    assert response.status_code == 401


def test_login_invalid_user(client):
    response = client.post(
        "/login",
        data={"username": "nonexistent@test.com", "password": "password123"},
    )
    assert response.status_code == 401


def test_create_first_admin(client, db_session):
    response = client.post(
        "/admin", json={"email": "newadmin@test.com", "senha": "securepassword"}
    )
    assert response.status_code == 201

    # Try creating another one, it should fail
    response2 = client.post(
        "/admin", json={"email": "secondadmin@test.com", "senha": "securepassword"}
    )
    assert response2.status_code == 400
