from typing import Iterable, Optional

from sqlalchemy.orm import Session

from app.models.bairro import Bairro
from app.schemas.bairro import BairroCreate


def criar_bairro(db: Session, bairro: BairroCreate) -> Bairro:
    """Cria um novo objeto Bairro e persiste no banco de dados."""
    novo = Bairro(nome=bairro.nome, cidade=bairro.cidade)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


def listar_bairros(db: Session) -> Iterable[Bairro]:
    """Retorna todos os bairros cadastrados no banco de dados."""
    return db.query(Bairro).all()


def atualizar_bairro(
    db: Session, bairro_id: int, dados: BairroCreate
) -> Optional[Bairro]:
    """Atualiza os dados de um bairro existente, se ele existir."""
    bairro_obj = db.get(Bairro, bairro_id)
    if bairro_obj is None:
        return None
    bairro_obj.nome = dados.nome
    bairro_obj.cidade = dados.cidade
    db.commit()
    db.refresh(bairro_obj)
    return bairro_obj


def deletar_bairro(db: Session, bairro_id: int) -> bool:
    """Remove um bairro do banco de dados, retornando True se excluído."""
    bairro_obj = db.get(Bairro, bairro_id)
    if bairro_obj is None:
        return False
    db.delete(bairro_obj)
    db.commit()
    return True
