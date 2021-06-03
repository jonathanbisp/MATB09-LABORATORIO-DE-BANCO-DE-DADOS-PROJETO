from typing import Optional

from pydantic import BaseModel

class Cliente(BaseModel):
    cpf: str
    nomecompleto: str
    pnome: str
    unome: str
    anonasc: str
    telcomercial: Optional[str] = None
    telpessoal: str
    email: str
    senha: str
    imglink: Optional[str] = None


class Nome(BaseModel):
    nome: str


class CPF(BaseModel):
    cpf: str


class Email(BaseModel):
    email: str