from pydantic import BaseModel, ConfigDict


class CeuCreate(BaseModel):
    nome: str
    bairro: str
    endereco: str


class CeuResponse(BaseModel):
    id: int
    nome: str
    bairro: str
    endereco: str

    model_config = ConfigDict(from_attributes=True)
