from pydantic import BaseModel
from datetime import date

class AtividadeCreate(BaseModel):
    titulo: str
    descricao: str
    data: date
    ceu_id: int

class AtividadeResponse(BaseModel):
    id: int
    descricao: str
    data: date
    ceu_id: int

    class Config:
        orm_mode = True