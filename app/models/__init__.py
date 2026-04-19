"""Pacote de modelos SQLAlchemy."""

from app.models.bairro import Bairro
from app.models.curso import Curso
from app.models.atividade import Atividade

__all__ = ["Bairro", "Curso", "Atividade"]
