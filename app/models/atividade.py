from sqlalchemy import Column, ForeignKey, Integer, String

from app.database import Base


class Atividade(Base):
    """Modelo de atividade vinculado a um curso."""

    __tablename__ = "atividades"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    curso_id = Column(Integer, ForeignKey("cursos.id"), nullable=True)
