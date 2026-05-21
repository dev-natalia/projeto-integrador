from fastapi import FastAPI

from app.database import Base, engine
from app.routes.ceu_routes import router as ceu_router
from app.routes.curso_routes import router as curso_router
from app.routes.atividade_routes import router as atividade_router
from app.models import ceu, curso, atividade

app = FastAPI(title="Projeto Integrador API", version="1.0")

app.include_router(ceu_router)
app.include_router(curso_router)
app.include_router(atividade_router)
Base.metadata.create_all(bind=engine)


@app.get("/", response_model=dict)
def root() -> dict[str, str]:
    """Retorna um status simples da API."""
    return {"msg": "API funcionando"}
