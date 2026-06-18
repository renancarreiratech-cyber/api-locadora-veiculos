from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_inicio():
    resposta = client.get("/")
    assert resposta.status_code == 200


def test_teste_banco():
    resposta = client.get("/teste-banco")
    assert resposta.status_code == 200


def test_listar_clientes():
    resposta = client.get("/clientes/")
    assert resposta.status_code == 200


def test_listar_veiculos():
    resposta = client.get("/veiculos/")
    assert resposta.status_code == 200


def test_listar_locacoes():
    resposta = client.get("/locacoes/")
    assert resposta.status_code == 200


def test_listar_historicos():
    resposta = client.get("/historicos/")
    assert resposta.status_code == 200


def test_docs():
    resposta = client.get("/docs")
    assert resposta.status_code == 200


def test_openapi():
    resposta = client.get("/openapi.json")
    assert resposta.status_code == 200


def test_redoc():
    resposta = client.get("/redoc")
    assert resposta.status_code == 200


def test_nao_encontrado():
    resposta = client.get("/rota_inexistente")
    assert resposta.status_code == 404