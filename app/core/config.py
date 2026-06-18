from dotenv import load_dotenv
import os

# Carrega as variáveis do .env
load_dotenv()

# URL do banco
DATABASE_URL = os.getenv("DATABASE_URL")