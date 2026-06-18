from app.models.cliente import Cliente
from app.repositories.cliente_repository import ClienteRepository


class ClienteService:

    def __init__(self):
        self.repository = ClienteRepository()

    # Cadastra um novo cliente
    def criar(self, db, dados):
        cliente = Cliente(
            nome=dados.nome,
            email=dados.email,
            telefone=dados.telefone
        )

        return self.repository.criar(db, cliente)

    # Lista todos os clientes
    def listar(self, db):
        return self.repository.listar(db)