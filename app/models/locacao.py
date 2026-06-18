from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.core.database import Base


# Modelo da tabela de locações
class Locacao(Base):
    __tablename__ = "locacoes"

    id = Column(Integer, primary_key=True, index=True)

    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    veiculo_id = Column(Integer, ForeignKey("veiculos.id"))

    data_locacao = Column(Date, nullable=False)
    data_devolucao = Column(Date, nullable=False)

    status = Column(String(20), default="ATIVA")

    cliente = relationship("Cliente", back_populates="locacoes")
    veiculo = relationship("Veiculo", back_populates="locacoes")
    historicos = relationship("HistoricoLocacao", back_populates="locacao")