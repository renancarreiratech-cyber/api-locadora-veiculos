from app.models.veiculo import Veiculo
from app.repositories.veiculo_repository import VeiculoRepository


class VeiculoService:

    def __init__(self):
        self.repository = VeiculoRepository()

    # Cadastra um novo veículo
    def criar(self, db, dados):
        veiculo = Veiculo(
            modelo=dados.modelo,
            marca=dados.marca,
            placa=dados.placa
        )

        return self.repository.criar(db, veiculo)

    # Lista todos os veículos
    def listar(self, db):
        return self.repository.listar(db)