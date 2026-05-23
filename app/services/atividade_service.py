from typing import Iterable, Optional
from datetime import date

from sqlalchemy.orm import Session

from app.models.atividade import Atividade
from app.schemas.atividade import AtividadeCreate, AtividadeResponse

def criar_atividade(db: Session, atividade: AtividadeCreate) -> Atividade:
    """Cria um novo objeto Atividade e persiste no banco de dados."""
    registro = Atividade(**atividade.model_dump())
    db.add(registro)
    db.commit()
    db.refresh(registro)
    return registro

def listar_atividades(db: Session, ceu_id: Optional[int] = None, data_filtro: Optional[date] = None) -> Iterable[Atividade]:
    """Retorna atividades com base nos filtros opcionais."""
    query = db.query(Atividade)
    if ceu_id is not None:
        query = query.filter(Atividade.ceu_id == ceu_id)
    if data_filtro is not None:
        query = query.filter(Atividade.data == data_filtro)
    return query.all()

def atualizar_atividade(db: Session, atividade_id: int, dados: AtividadeCreate) -> Optional[Atividade]:
    """Atualiza os dados de uma atividade existente, se ela existir."""
    atividade_obj = db.get(Atividade, atividade_id)
    if atividade_obj is None:
        return None
    atividade_obj.titulo = dados.titulo
    atividade_obj.descricao = dados.descricao
    atividade_obj.data = dados.data
    atividade_obj.ceu_id = dados.ceu_id
    db.commit()
    db.refresh(atividade_obj)
    return atividade_obj

def deletar_atividade(db: Session, atividade_id: int) -> bool:
    """Remove uma atividade do banco de dados, retornando True se excluído."""
    atividade_obj = db.get(Atividade, atividade_id)
    if atividade_obj is None:
        return False
    db.delete(atividade_obj)
    db.commit()
    return True