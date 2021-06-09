from typing import Optional

from pydantic import BaseModel

class Funcionario(BaseModel):
    cpf: str
    nomecompleto: str  
    anonasc: str
    cargo: str
    email: str
    senha: str
    imglink: Optional[str] = None
    fk_codigo_supervisor: Optional[int] = None



class Nome(BaseModel):
    nome: str


class CPF(BaseModel):
    cpf: str


class Email(BaseModel):
    email: str