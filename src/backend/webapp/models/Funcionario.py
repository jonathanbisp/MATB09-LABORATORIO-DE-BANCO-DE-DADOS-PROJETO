from typing import Optional

from pydantic import BaseModel

class Funcionario(BaseModel):
    cpf: str
    codigo: str  
    pnome: str
    unome: str
    anonasc: str
    cargo: str
    nomecompleto: str
    email: str
    senha: str
    imglink: Optional[str] = None
    fk_cpf_supervisor: str
    fk_codigo_supervisor: str
    fk_cliente_cpf: str


class Nome(BaseModel):
    nome: str


class CPF(BaseModel):
    cpf: str


class Email(BaseModel):
    email: str