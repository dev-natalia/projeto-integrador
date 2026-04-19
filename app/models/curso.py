from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database import Base


class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    descricao = Column(String)
    data_inicio = Column(Date)
    data_fim = Column(Date)
    bairro_id = Column(Integer, ForeignKey("bairros.id"))
