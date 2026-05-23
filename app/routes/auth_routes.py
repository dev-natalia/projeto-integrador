from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.admin import Admin
from app.schemas.admin import AdminCreate, Token
from app.auth import (
    create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    get_password_hash,
    verify_password,
)

router = APIRouter(tags=["Auth"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def authenticate_admin_db(db: Session, email: str, password: str):
    admin = db.query(Admin).filter(Admin.email == email).first()
    if not admin:
        return False
    if not verify_password(password, admin.senha_hash):
        return False
    return admin


@router.post("/login", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    admin = authenticate_admin_db(db, form_data.username, form_data.password)
    if not admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": admin.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/admin", status_code=201)
def create_first_admin(admin_data: AdminCreate, db: Session = Depends(get_db)):
    """Rota auxiliar para criar o primeiro admin. Em um sistema real seria mais protegida."""
    admin_exists = db.query(Admin).first()
    if admin_exists:
        raise HTTPException(
            status_code=400, detail="Admin já existe. Rota desabilitada."
        )

    hashed_password = get_password_hash(admin_data.senha)
    novo_admin = Admin(email=admin_data.email, senha_hash=hashed_password)
    db.add(novo_admin)
    db.commit()
    return {"message": "Admin criado com sucesso"}
