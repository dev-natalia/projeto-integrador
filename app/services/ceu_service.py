from typing import Iterable, Optional

from sqlalchemy.orm import Session

from app.models.ceu import Ceu
from app.schemas.ceu import CeuCreate


def criar_ceu(db: Session, ceu: CeuCreate) -> Ceu:
    """Cria um novo objeto Ceu e persiste no banco de dados."""
    novo = Ceu(nome=ceu.nome, bairro=ceu.bairro, endereco=ceu.endereco)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


def listar_ceus(db: Session) -> Iterable[Ceu]:
    """Retorna todos os ceus cadastrados no banco de dados."""
    return db.query(Ceu).all()


def atualizar_ceu(db: Session, ceu_id: int, dados: CeuCreate) -> Optional[Ceu]:
    """Atualiza os dados de um ceu existente, se ele existir."""
    ceu_obj = db.get(Ceu, ceu_id)
    if ceu_obj is None:
        return None
    ceu_obj.nome = dados.nome
    ceu_obj.bairro = dados.bairro
    ceu_obj.endereco = dados.endereco
    db.commit()
    db.refresh(ceu_obj)
    return ceu_obj


def deletar_ceu(db: Session, ceu_id: int) -> bool:
    """Remove um ceu do banco de dados, retornando True se excluído."""
    ceu_obj = db.get(Ceu, ceu_id)
    if ceu_obj is None:
        return False
    db.delete(ceu_obj)
    db.commit()
    return True
