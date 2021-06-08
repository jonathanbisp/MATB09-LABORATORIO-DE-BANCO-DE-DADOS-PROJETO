from typing import Optional

from pydantic import BaseModel

class Aluga(BaseModel):
    fk_cliente_cpf: str
    fk_veiculo_revavam: str
    fk_veiculo_numchassi: str
    fk_funcionario_codigo: str
    fk_seguro_codigo: str
    datalocacao: str
    datadevolucao: str
    status: str
    valor: str
    parcelas: str
    parcelaspagas: str
    



class fk_cliente_cpf(BaseModel):
    fk_cliente_cpf: str


class fk_veiculo_revavam(BaseModel):
    fk_veiculo_revavam: str


class fk_veiculo_numchassi(BaseModel):
    fk_veiculo_numchassi: str