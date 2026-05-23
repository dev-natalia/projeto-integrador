from sqlalchemy import Column, ForeignKey, Integer, String, Date

from app.database import Base


class Atividade(Base):
    """Modelo de atividade vinculado a um ceu."""

    __tablename__ = "atividades"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    data = Column(Date)
    ceu_id = Column(Integer, ForeignKey("ceu.id"), nullable=True)
