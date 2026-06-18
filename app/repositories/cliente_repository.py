from sqlalchemy.orm import Session

from app.models.cliente import Cliente


class ClienteRepository:

    # Salva um cliente no banco
    def criar(self, db: Session, cliente: Cliente):
        db.add(cliente)
        db.commit()
        db.refresh(cliente)

        return cliente

    # Lista todos os clientes
    def listar(self, db: Session):
        return db.query(Cliente).all()

    # Busca um cliente pelo ID
    def buscar_por_id(self, db: Session, cliente_id: int):
        return db.query(Cliente).filter(
            Cliente.id == cliente_id
        ).first()

    # Atualiza um cliente
    def atualizar(self, db: Session, cliente: Cliente):
        db.commit()
        db.refresh(cliente)

        return cliente