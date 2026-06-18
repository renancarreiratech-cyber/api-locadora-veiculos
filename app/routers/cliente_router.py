from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.cliente_schema import ClienteCreate
from app.schemas.cliente_schema import ClienteResponse
from app.services.cliente_service import ClienteService

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)

service = ClienteService()


# Cadastra um cliente
@router.post("/", response_model=ClienteResponse)
def criar_cliente(
    cliente: ClienteCreate,
    db: Session = Depends(get_db)
):
    return service.criar(db, cliente)


# Lista todos os clientes
@router.get("/", response_model=list[ClienteResponse])
def listar_clientes(
    db: Session = Depends(get_db)
):
    return service.listar(db)