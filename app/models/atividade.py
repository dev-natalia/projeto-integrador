from sqlalchemy import Column, ForeignKey, Integer, String, Date, Time

from app.database import Base


class Atividade(Base):
    """Modelo de atividade vinculado a um ceu."""

    __tablename__ = "atividades"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    data = Column(Date, nullable=False)
    hora_inicio = Column(Time, nullable=False)
    hora_fim = Column(Time, nullable=True)
    ceu_id = Column(Integer, ForeignKey("ceu.id"), nullable=True)
