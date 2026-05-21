from pydantic import BaseModel
from datetime import date

class CursoCreate(BaseModel):
    titulo: str
    descricao: str
    data_inicio: date
    data_fim: date
    bairro_id: int


class CursoResponse(BaseModel):
    id: int
    titulo: str
    descricao: str
    data_inicio: date
    data_fim: date
    bairro_id: int

    class Config:
        orm_mode = True