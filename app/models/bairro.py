from sqlalchemy import Column, Integer, String
from app.database import Base


class Bairro(Base):
    __tablename__ = "bairros"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    cidade = Column(String)
