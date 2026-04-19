from sqlalchemy import Column, Integer, String
from app.database import Base


class Ceu(Base):
    __tablename__ = "ceu"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    bairro = Column(String)
    endereco = Column(String)
