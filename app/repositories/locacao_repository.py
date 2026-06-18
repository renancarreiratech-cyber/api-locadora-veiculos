from sqlalchemy.orm import Session

from app.models.locacao import Locacao


class LocacaoRepository:

    # Salva uma locação no banco
    def criar(self, db: Session, locacao: Locacao):
        db.add(locacao)
        db.commit()
        db.refresh(locacao)

        return locacao

    # Lista todas as locações
    def listar(self, db: Session):
        return db.query(Locacao).all()

    # Busca uma locação pelo ID
    def buscar_por_id(self, db: Session, locacao_id: int):
        return db.query(Locacao).filter(
            Locacao.id == locacao_id
        ).first()

    # Atualiza uma locação
    def atualizar(self, db: Session, locacao: Locacao):
        db.commit()
        db.refresh(locacao)

        return locacao