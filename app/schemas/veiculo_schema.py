from pydantic import BaseModel


# Dados para cadastrar um veículo
class VeiculoCreate(BaseModel):
    modelo: str
    marca: str
    placa: str


# Dados retornados pela API
class VeiculoResponse(BaseModel):
    id: int
    modelo: str
    marca: str
    placa: str
    disponivel: bool

    class Config:
        from_attributes = True