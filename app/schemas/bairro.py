from pydantic import BaseModel


class BairroCreate(BaseModel):
    nome: str
    cidade: str


class BairroResponse(BaseModel):
    id: int
    nome: str
    cidade: str

    class Config:
        orm_mode = True
