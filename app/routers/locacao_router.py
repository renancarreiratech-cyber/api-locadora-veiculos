from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.locacao_schema import LocacaoCreate
from app.schemas.locacao_schema import LocacaoResponse
from app.services.locacao_service import LocacaoService

router = APIRouter(
    prefix="/locacoes",
    tags=["Locações"]
)

service = LocacaoService()


# Cadastra uma locação
@router.post("/", response_model=LocacaoResponse)
def criar_locacao(
    locacao: LocacaoCreate,
    db: Session = Depends(get_db)
):
    return service.criar(db, locacao)


# Lista todas as locações
@router.get("/", response_model=list[LocacaoResponse])
def listar_locacoes(
    db: Session = Depends(get_db)
):
    return service.listar(db)