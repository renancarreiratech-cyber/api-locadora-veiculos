from fastapi import HTTPException

from app.models.locacao import Locacao

from app.repositories.cliente_repository import ClienteRepository
from app.repositories.veiculo_repository import VeiculoRepository
from app.repositories.locacao_repository import LocacaoRepository


class LocacaoService:

    def __init__(self):
        self.repository = LocacaoRepository()
        self.cliente_repository = ClienteRepository()
        self.veiculo_repository = VeiculoRepository()

    # Cadastra uma nova locação
    def criar(self, db, dados):

        cliente = self.cliente_repository.buscar_por_id(
            db,
            dados.cliente_id
        )

        if not cliente:
            raise HTTPException(
                status_code=404,
                detail="Cliente não encontrado."
            )

        veiculo = self.veiculo_repository.buscar_por_id(
            db,
            dados.veiculo_id
        )

        if not veiculo:
            raise HTTPException(
                status_code=404,
                detail="Veículo não encontrado."
            )

        if not veiculo.disponivel:
            raise HTTPException(
                status_code=400,
                detail="Veículo indisponível."
            )

        veiculo.disponivel = False
        self.veiculo_repository.atualizar(db, veiculo)

        locacao = Locacao(
            cliente_id=dados.cliente_id,
            veiculo_id=dados.veiculo_id,
            data_locacao=dados.data_locacao,
            data_devolucao=dados.data_devolucao,
            status="ATIVA"
        )

        return self.repository.criar(db, locacao)

    # Lista todas as locações
    def listar(self, db):
        return self.repository.listar(db)