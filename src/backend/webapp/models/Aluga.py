from pydantic import BaseModel
from typing import Optional

class Aluga(BaseModel):
    fk_cliente_cpf: str
    fk_veiculo_renavam: str
    fk_veiculo_numchassi: str
    fk_funcionario_codigo: str
    fk_seguro_codigo: Optional[str] = None
    datalocacao: str
    datadevolucao: str
    status: str
    valor: str
    parcelas: str
    parcelaspagas: str
    

class fk_cliente_cpf(BaseModel):
    fk_cliente_cpf: str


class fk_veiculo_renavam(BaseModel):
    fk_veiculo_renavam: str


class fk_veiculo_numchassi(BaseModel):
    fk_veiculo_numchassi: str