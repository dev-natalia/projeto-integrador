from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import date, time


class AtividadeCreate(BaseModel):
    titulo: str
    descricao: str
    data: date
    hora_inicio: time
    hora_fim: Optional[time] = None
    ceu_id: int


class AtividadeResponse(BaseModel):
    id: int
    titulo: str
    descricao: str
    data: date
    hora_inicio: time
    hora_fim: Optional[time] = None
    ceu_id: int

    model_config = ConfigDict(from_attributes=True)
