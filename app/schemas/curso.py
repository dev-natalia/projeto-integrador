from pydantic import BaseModel, ConfigDict
from datetime import date

class CursoCreate(BaseModel):
    titulo: str
    descricao: str
    data_inicio: date
    data_fim: date
    ceu_id: int


class CursoResponse(BaseModel):
    id: int
    titulo: str
    descricao: str
    data_inicio: date
    data_fim: date
    ceu_id: int

    model_config = ConfigDict(from_attributes=True)