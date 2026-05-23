from typing import Generator, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.ceu import CeuCreate, CeuResponse
from app.services import ceu_service
from app.auth import get_current_admin
from app.models.admin import Admin

router = APIRouter(tags=["CEU"])


def get_db() -> Generator[Session, None, None]:
    """Cria e encerra a sessão do banco de dados para cada requisição."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/ceu", response_model=CeuResponse, status_code=201)
def criar(ceu: CeuCreate, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)) -> CeuResponse:
    """Cria um novo ceu no banco de dados."""
    return ceu_service.criar_ceu(db, ceu)


@router.get("/ceu", response_model=List[CeuResponse])
def listar_todos(db: Session = Depends(get_db)) -> List[CeuResponse]:
    """Retorna a lista de ceus cadastrados."""
    return ceu_service.listar_ceus(db)


@router.put("/ceu/{id}", response_model=CeuResponse)
def atualizar_ceu(id: int, ceu: CeuCreate, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)) -> CeuResponse:
    """Atualiza dados de um ceu existente."""
    return ceu_service.atualizar_ceu(db, id, ceu)


@router.delete("/ceu/{id}", response_model=bool)
def deletar_ceu(id: int, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)) -> bool:
    """Deletar ceu do banco de dados."""
    return ceu_service.deletar_ceu(db, id)
