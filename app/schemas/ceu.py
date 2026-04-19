from pydantic import BaseModel


class CeuCreate(BaseModel):
    nome: str
    bairro: str
    endereco: str


class CeuResponse(BaseModel):
    id: int
    nome: str
    bairro: str
    endereco: str

    class Config:
        orm_mode = True
