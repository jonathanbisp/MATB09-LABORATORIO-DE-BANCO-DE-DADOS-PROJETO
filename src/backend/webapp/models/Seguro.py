from typing import Optional

from pydantic import BaseModel

class Seguro(BaseModel):
    nome: str  
    descricao: str
    valor: str
    fk_veiculo_renavam: str
    fk_veiculo_numchassi: str


class Nome(BaseModel):
    nome: str


class Codigo(BaseModel):
    codigo: str


class Valor(BaseModel):
    valor: str