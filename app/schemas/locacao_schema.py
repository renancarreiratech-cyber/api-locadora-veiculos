from datetime import date

from pydantic import BaseModel


# Dados para cadastrar uma locação
class LocacaoCreate(BaseModel):
    cliente_id: int
    veiculo_id: int
    data_locacao: date
    data_devolucao: date


# Dados retornados pela API
class LocacaoResponse(BaseModel):
    id: int
    cliente_id: int
    veiculo_id: int
    data_locacao: date
    data_devolucao: date
    status: str

    class Config:
        from_attributes = True