from fastapi import FastAPI

from app.database import Base, engine
from app.routes.ceu_routes import router as bairro_router
from app.models import ceu, curso, atividade

app = FastAPI(title="Projeto Integrador API", version="1.0")

app.include_router(bairro_router)
Base.metadata.create_all(bind=engine)


@app.get("/", response_model=dict)
def root() -> dict[str, str]:
    """Retorna um status simples da API."""
    return {"msg": "API funcionando"}
