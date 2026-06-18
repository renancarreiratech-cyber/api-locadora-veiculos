from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.veiculo_schema import VeiculoCreate
from app.schemas.veiculo_schema import VeiculoResponse
from app.services.veiculo_service import VeiculoService

router = APIRouter(
    prefix="/veiculos",
    tags=["Veículos"]
)

service = VeiculoService()


# Cadastra um veículo
@router.post("/", response_model=VeiculoResponse)
def criar_veiculo(
    veiculo: VeiculoCreate,
    db: Session = Depends(get_db)
):
    return service.criar(db, veiculo)


# Lista todos os veículos
@router.get("/", response_model=list[VeiculoResponse])
def listar_veiculos(
    db: Session = Depends(get_db)
):
    return service.listar(db)