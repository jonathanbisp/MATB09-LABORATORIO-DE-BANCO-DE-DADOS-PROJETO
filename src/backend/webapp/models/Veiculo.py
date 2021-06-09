from typing import Optional

from pydantic import BaseModel


class Veiculo(BaseModel):
    renavam: str
    numchassi: str
    modelo: str
    anofabricacao: str
    imglink: Optional[str] = None


class Renavam(BaseModel):
    renavam: str


class Modelo(BaseModel):
    modelo: str


class Numchassi(BaseModel):
    numchassi: str