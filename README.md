# API Locadora de Veículos

Projeto desenvolvido para a disciplina de Desenvolvimento de APIs.

## Tecnologias

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Docker
- Pytest

## Funcionalidades

- Cadastro de clientes
- Cadastro de veículos
- Cadastro de locações
- Consulta de clientes
- Consulta de veículos
- Consulta de locações
- Histórico de locações

## Executar

Instalar dependências

```bash
pip install -r requirements.txt
```

Executar a API

```bash
uvicorn app.main:app --reload --port 8001
```

Documentação

http://localhost:8001/docs

Executar testes

```bash
python -m pytest
```