from typing import Iterable, Optional

from sqlalchemy.orm import Session

from app.models.curso import Curso
from app.schemas.curso import CursoCreate


def criar_curso(db: Session, curso: CursoCreate) -> Curso:
    """Cria um novo objeto Curso e persiste no banco de dados."""
    novo = Curso(titulo=curso.titulo, descricao=curso.descricao, data_inicio=curso.data_inicio, data_fim=curso.data_fim, bairro_id=curso.bairro_id)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


def listar_cursos(db: Session) -> Iterable[Curso]:
    """Retorna todos os cursos cadastrados no banco de dados."""
    return db.query(Curso).all()


def atualizar_curso(db: Session, curso_id: int, dados: CursoCreate) -> Optional[Curso]:
    """Atualiza os dados de um curso existente, se ele existir."""
    curso_obj = db.get(Curso, curso_id)
    if curso_obj is None:
        return None
    curso_obj.titulo = dados.titulo
    curso_obj.descricao = dados.descricao
    curso_obj.data_inicio = dados.data_inicio
    curso_obj.data_fim = dados.data_fim
    curso_obj.bairro_id = dados.bairro_id

    db.commit()
    db.refresh(curso_obj)
    return curso_obj

def buscar_por_ceu(db: Session, ceu_id: int) -> Iterable[Curso]:
    """Retorna todos cursos filtrados por ceu_id."""
    return db.query(Curso).filter(Curso.bairro_id == ceu_id).all()

def deletar_curso(db: Session, curso_id: int) -> bool:
    """Remove um curso do banco de dados, retornando True se excluído."""
    curso_obj = db.get(Curso, curso_id)
    if curso_obj is None:
        return False
    db.delete(curso_obj)
    db.commit()
    return True