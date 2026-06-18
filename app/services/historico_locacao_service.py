from app.repositories.historico_locacao_repository import (
    HistoricoLocacaoRepository
)


class HistoricoLocacaoService:

    def __init__(self):
        self.repository = HistoricoLocacaoRepository()

    # Lista todos os históricos
    def listar(self, db):
        return self.repository.listar(db)