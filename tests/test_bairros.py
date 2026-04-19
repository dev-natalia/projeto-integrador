from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.bairro import BairroCreate
from app.services.bairro_service import criar_bairro


def test_criar_bairro() -> None:
    """Verifica se um bairro pode ser criado corretamente."""
    db: Session = SessionLocal()
    try:
        bairro = criar_bairro(db, BairroCreate(nome="Centro", cidade="SP"))
        assert bairro.id is not None
        assert bairro.nome == "Centro"
        assert bairro.cidade == "SP"
    finally:
        db.close()
