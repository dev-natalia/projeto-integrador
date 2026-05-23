from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from app.database import Base


class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    data = Column(Date, nullable=False)
    hora_inicio = Column(Time, nullable=False)
    hora_fim = Column(Time, nullable=True)
    ceu_id = Column(Integer, ForeignKey("ceu.id"))
