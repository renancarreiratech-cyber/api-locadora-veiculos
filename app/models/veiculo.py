from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.core.database import Base


# Modelo da tabela de veículos
class Veiculo(Base):
    __tablename__ = "veiculos"

    id = Column(Integer, primary_key=True, index=True)

    modelo = Column(String(100), nullable=False)
    marca = Column(String(100), nullable=False)
    placa = Column(String(15), unique=True, nullable=False)
    disponivel = Column(Boolean, default=True)

    locacoes = relationship("Locacao", back_populates="veiculo")