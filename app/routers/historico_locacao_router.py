from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.historico_locacao_schema import HistoricoLocacaoResponse
from app.services.historico_locacao_service import HistoricoLocacaoService

router = APIRouter(
    prefix="/historicos",
    tags=["Histórico"]
)

service = HistoricoLocacaoService()


# Lista todos os históricos
@router.get("/", response_model=list[HistoricoLocacaoResponse])
def listar_historicos(
    db: Session = Depends(get_db)
):
    return service.listar(db)