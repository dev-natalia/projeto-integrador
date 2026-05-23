from pydantic import BaseModel, ConfigDict
from datetime import date

class AtividadeCreate(BaseModel):
    titulo: str
    descricao: str
    data: date
    ceu_id: int

class AtividadeResponse(BaseModel):
    id: int
    titulo: str
    descricao: str
    data: date
    ceu_id: int

    model_config = ConfigDict(from_attributes=True)