from pydantic import BaseModel


# Dados para cadastrar um cliente
class ClienteCreate(BaseModel):
    nome: str
    email: str
    telefone: str


# Dados retornados pela API
class ClienteResponse(BaseModel):
    id: int
    nome: str
    email: str
    telefone: str
    ativo: bool

    class Config:
        from_attributes = True