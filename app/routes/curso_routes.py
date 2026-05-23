from typing import Generator, List
from datetime import date

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.curso import CursoCreate, CursoResponse
from app.services import curso_service
from app.auth import get_current_admin
from app.models.admin import Admin

router = APIRouter(tags=["Cursos"])


def get_db() -> Generator[Session, None, None]:
    """Cria e encerra a sessão do banco de dados para cada requisição."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/cursos", response_model=CursoResponse, status_code=201)
def criar_curso(curso: CursoCreate, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)) -> CursoResponse:
    """Cria um novo curso no banco de dados."""
    return curso_service.criar_curso(db, curso)

@router.get("/cursos", response_model=List[CursoResponse])
def listar_cursos(ceu_id: int | None = None, data_filtro: date | None = None, db: Session = Depends(get_db)) -> List[CursoResponse]:
    """Retorna uma lista com todos os cursos cadastrados no banco de dados ou filtrados se ceu_id ou data_filtro for passado."""
    return curso_service.listar_cursos(db, ceu_id=ceu_id, data_filtro=data_filtro)

@router.put("/cursos/{curso_id}", response_model=CursoResponse)
def atualizar_curso(curso_id: int, novos_dados: CursoCreate, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)) -> CursoResponse:
    """Atualiza curso existente"""
    return curso_service.atualizar_curso(db, curso_id, novos_dados)

@router.delete("/cursos/{curso_id}", response_model=bool)
def deletar_curso(curso_id: int, db: Session = Depends(get_db), current_admin: Admin = Depends(get_current_admin)) -> bool:
    """Deletar curso do banco de dados"""
    return curso_service.deletar_curso(db, curso_id)