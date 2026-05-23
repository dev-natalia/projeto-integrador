from typing import Generator, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.curso import CursoCreate, CursoResponse
from app.services import curso_service

router = APIRouter(tags=["Cursos"])


def get_db() -> Generator[Session, None, None]:
    """Cria e encerra a sessão do banco de dados para cada requisição."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/cursos", response_model=CursoResponse, status_code=201)
def criar_curso(curso: CursoCreate, db: Session = Depends(get_db)) -> CursoResponse:
    """Cria um novo curso no banco de dados."""
    return curso_service.criar_curso(db, curso)

# TODO: Adicionar filtro de data.
@router.get("/cursos", response_model=List[CursoResponse])
def listar_cursos(ceu_id: int | None = None, db: Session = Depends(get_db)) -> List[CursoResponse]:
    """Retorna uma lista com todos os cursos cadastrados no banco de dados ou filtrados se ceu_id for passado."""

    if ceu_id is not None:
        return curso_service.buscar_por_ceu(db, ceu_id)
    return curso_service.listar_cursos(db)

@router.put("/cursos/{curso_id}", response_model=CursoResponse)
def atualizar_curso(curso_id: int, novos_dados: CursoCreate, db: Session = Depends(get_db)) -> CursoResponse:
    """Atualiza curso existente"""
    return curso_service.atualizar_curso(db, curso_id, novos_dados)

@router.delete("/cursos/{curso_id}", response_model=bool)
def deletar_curso(curso_id: int, db: Session = Depends(get_db)) -> bool:
    """Deletar curso do banco de dados"""
    return curso_service.deletar_curso(db, curso_id)