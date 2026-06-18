from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.core.database import Base


# Modelo da tabela de histórico
class HistoricoLocacao(Base):
    __tablename__ = "historico_locacoes"

    id = Column(Integer, primary_key=True, index=True)

    locacao_id = Column(Integer, ForeignKey("locacoes.id"))

    status_anterior = Column(String(20), nullable=False)
    status_novo = Column(String(20), nullable=False)

    data_alteracao = Column(Date, nullable=False)

    locacao = relationship("Locacao", back_populates="historicos")