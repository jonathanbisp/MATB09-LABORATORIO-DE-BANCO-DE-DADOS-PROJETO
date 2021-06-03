from typing import Optional

from pydantic import BaseModel


class Veiculo(BaseModel):
    revavam: str
    numchassi: str
    modelo: str
    anofabricacao: str
    imglink: Optional[str] = None


class Revavam(BaseModel):
    revavam: str


class Modelo(BaseModel):
    modelo: str


class Numchassi(BaseModel):
    numchassi: str