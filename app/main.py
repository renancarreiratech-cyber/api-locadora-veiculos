from fastapi import FastAPI
from sqlalchemy import text

from app.core.database import Base
from app.core.database import engine

from app.models.cliente import Cliente
from app.models.veiculo import Veiculo
from app.models.locacao import Locacao
from app.models.historico_locacao import HistoricoLocacao

from app.routers.cliente_router import router as cliente_router
from app.routers.veiculo_router import router as veiculo_router
from app.routers.locacao_router import router as locacao_router
from app.routers.historico_locacao_router import router as historico_router

# Cria as tabelas no banco
# Base.metadata.create_all(bind=engine)

# Cria a aplicação
app = FastAPI(
    title="API Locadora de Veículos",
    version="1.0.0"
)

# Registra as rotas
app.include_router(cliente_router)
app.include_router(veiculo_router)
app.include_router(locacao_router)
app.include_router(historico_router)


# Página inicial
@app.get("/")
def inicio():
    return {
        "mensagem": "API da Locadora de Veículos funcionando!"
    }


# Testa a conexão com o banco
@app.get("/teste-banco")
def teste_banco():

    try:
        with engine.connect() as conexao:
            conexao.execute(text("SELECT 1"))

        return {
            "status": "Conectado ao PostgreSQL!"
        }

    except Exception as erro:
        return {
            "status": "Erro na conexão",
            "erro": str(erro)
        }