from sqlalchemy.orm import Session

from app.models.veiculo import Veiculo


class VeiculoRepository:

    # Salva um veículo no banco
    def criar(self, db: Session, veiculo: Veiculo):
        db.add(veiculo)
        db.commit()
        db.refresh(veiculo)

        return veiculo

    # Lista todos os veículos
    def listar(self, db: Session):
        return db.query(Veiculo).all()

    # Busca um veículo pelo ID
    def buscar_por_id(self, db: Session, veiculo_id: int):
        return db.query(Veiculo).filter(
            Veiculo.id == veiculo_id
        ).first()

    # Atualiza um veículo
    def atualizar(self, db: Session, veiculo: Veiculo):
        db.commit()
        db.refresh(veiculo)

        return veiculo