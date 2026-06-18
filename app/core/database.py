from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import DATABASE_URL

# Cria a conexão com o banco
engine = create_engine(DATABASE_URL)

# Cria as sessões do banco
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base para os modelos
Base = declarative_base()


# Retorna uma sessão do banco
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()