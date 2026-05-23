from typing import Iterable, Optional
from datetime import date

from sqlalchemy.orm import Session

from app.models.curso import Curso
from app.schemas.curso import CursoCreate


def criar_curso(db: Session, curso: CursoCreate) -> Curso:
    """Cria um novo objeto Curso e persiste no banco de dados."""
    novo = Curso(
        titulo=curso.titulo,
        descricao=curso.descricao,
        data=curso.data,
        hora_inicio=curso.hora_inicio,
        hora_fim=curso.hora_fim,
        ceu_id=curso.ceu_id,
    )
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


def listar_cursos(
    db: Session, ceu_id: Optional[int] = None, data_filtro: Optional[date] = None
) -> Iterable[Curso]:
    """Retorna cursos com base nos filtros opcionais (ceu_id e data)."""
    query = db.query(Curso)
    if ceu_id is not None:
        query = query.filter(Curso.ceu_id == ceu_id)
    if data_filtro is not None:
        query = query.filter(Curso.data == data_filtro)
    return query.all()


def atualizar_curso(db: Session, curso_id: int, dados: CursoCreate) -> Optional[Curso]:
    """Atualiza os dados de um curso existente, se ele existir."""
    curso_obj = db.get(Curso, curso_id)
    if curso_obj is None:
        return None
    curso_obj.titulo = dados.titulo
    curso_obj.descricao = dados.descricao
    curso_obj.data = dados.data
    curso_obj.hora_inicio = dados.hora_inicio
    curso_obj.hora_fim = dados.hora_fim
    curso_obj.ceu_id = dados.ceu_id

    db.commit()
    db.refresh(curso_obj)
    return curso_obj


def deletar_curso(db: Session, curso_id: int) -> bool:
    """Remove um curso do banco de dados, retornando True se excluído."""
    curso_obj = db.get(Curso, curso_id)
    if curso_obj is None:
        return False
    db.delete(curso_obj)
    db.commit()
    return True
