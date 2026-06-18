from sqlalchemy.orm import Session

from app.models.historico_locacao import HistoricoLocacao


class HistoricoLocacaoRepository:

    # Salva um histórico no banco
    def criar(self, db: Session, historico: HistoricoLocacao):
        db.add(historico)
        db.commit()
        db.refresh(historico)

        return historico

    # Lista todos os históricos
    def listar(self, db: Session):
        return db.query(HistoricoLocacao).all()