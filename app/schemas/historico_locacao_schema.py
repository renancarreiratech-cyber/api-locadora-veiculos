from datetime import date

from pydantic import BaseModel


# Dados retornados pela API
class HistoricoLocacaoResponse(BaseModel):
    id: int
    locacao_id: int
    status_anterior: str
    status_novo: str
    data_alteracao: date

    class Config:
        from_attributes = True