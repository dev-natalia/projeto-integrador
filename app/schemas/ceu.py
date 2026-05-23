from pydantic import BaseModel, ConfigDict


class CeuCreate(BaseModel):
    nome: str
    bairro: str
    endereco: str
    telefone: str


class CeuResponse(BaseModel):
    id: int
    nome: str
    bairro: str
    endereco: str
    telefone: str

    model_config = ConfigDict(from_attributes=True)
