from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.ceu import CeuCreate
from app.services.ceu_service import criar_ceu


def test_criar_ceu() -> None:
    """Verifica se um ceu pode ser criado corretamente."""
    db: Session = SessionLocal()
    try:
        ceu = criar_ceu(
            db,
            CeuCreate(nome="Ceu Cidade Dutra", bairro="Cidade Dutra", endereco="xyz"),
        )
        assert ceu.id is not None
        assert ceu.nome == "Ceu Cidade Dutra"
        assert ceu.bairro == "Cidade Dutra"
        assert ceu.endereco == "xyz"
    finally:
        db.close()
