from typing import Generator, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.bairro import BairroCreate, BairroResponse
from app.services import bairro_service

router = APIRouter(tags=["Bairros"])


def get_db() -> Generator[Session, None, None]:
    """Cria e encerra a sessão do banco de dados para cada requisição."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/bairros", response_model=BairroResponse, status_code=201)
def criar(bairro: BairroCreate, db: Session = Depends(get_db)) -> BairroResponse:
    """Cria um novo bairro no banco de dados."""
    return bairro_service.criar_bairro(db, bairro)


@router.get("/bairros", response_model=List[BairroResponse])
def listar(db: Session = Depends(get_db)) -> List[BairroResponse]:
    """Retorna a lista de bairros cadastrados."""
    return bairro_service.listar_bairros(db)
