from typing import Generator, List
from datetime import date

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.atividade import AtividadeCreate, AtividadeResponse
from app.services import atividade_service
from app.auth import get_current_admin
from app.models.admin import Admin

router = APIRouter(tags=["Atividades"])

def get_db() -> Generator[Session, None, None]:
    """Cria e encerra a sessão do banco de dados para cada requisição."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/atividades", response_model=AtividadeResponse, status_code=201)
def criar_atividade(atividade: AtividadeCreate, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)) -> AtividadeResponse:
    """Cria uma nova atividade no banco de dados."""
    return atividade_service.criar_atividade(db, atividade)

@router.get("/atividades", response_model=List[AtividadeResponse])
def listar_atividades(ceu_id: int | None = None, data_filtro: date | None = None, db: Session = Depends(get_db)) -> List[AtividadeResponse]:
    """Retorna todas as atividades com base nos filtros passados."""
    return atividade_service.listar_atividades(db, ceu_id=ceu_id, data_filtro=data_filtro)

@router.put("/atividades/{id}", response_model=AtividadeResponse)
def atualizar_atividade(id: int, atividade: AtividadeCreate, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)) -> AtividadeResponse:
    """Atualiza dados de atividade existente."""
    return atividade_service.atualizar_atividade(db, id, atividade)

@router.delete("/atividades/{id}", response_model=bool)
def deletar_atividade(id: int, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)) -> bool:
    """Deletar atividade do banco de dados"""
    return atividade_service.deletar_atividade(db, id)