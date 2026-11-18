import requests
import time


def verificar_servico(nome, url):
    """
    Verifica se um serviço está disponível.
    Mede o tempo de resposta e retorna dados estruturados.
    """

    inicio = time.time()

    try:
        resposta = requests.get(url, timeout=10)

        tempo_resposta = round((time.time() - inicio) * 1000, 2)

        resultado = {
            "nome": nome,
            "url": url,
            "status_code": resposta.status_code,
            "tempo_resposta": tempo_resposta,
            "status": "ONLINE" if resposta.status_code < 400 else "OFFLINE",
            "erro": None
        }

        return resultado

    except requests.exceptions.Timeout:
        return {
            "nome": nome,
            "url": url,
            "status_code": None,
            "tempo_resposta": None,
            "status": "OFFLINE",
            "erro": "Tempo limite de conexão excedido"
        }

    except requests.exceptions.ConnectionError:
        return {
            "nome": nome,
            "url": url,
            "status_code": None,
            "tempo_resposta": None,
            "status": "OFFLINE",
            "erro": "Erro de conexão"
        }

    except requests.exceptions.RequestException as erro:
        return {
            "nome": nome,
            "url": url,
            "status_code": None,
            "tempo_resposta": None,
            "status": "OFFLINE",
            "erro": str(erro)
        }


def verificar_json(nome, url):
    """
    Consulta uma API e valida o retorno JSON.
    """

    try:
        resposta = requests.get(url, timeout=10)

        resposta.raise_for_status()

        dados = resposta.json()

        if isinstance(dados, dict) and "id" in dados:
            status = "ONLINE"
        else:
            status = "DADOS INVALIDOS"

        return {
            "nome": nome,
            "status": status,
            "dados": dados,
            "erro": None
        }

    except requests.exceptions.RequestException as erro:
        return {
            "nome": nome,
            "status": "OFFLINE",
            "dados": None,
            "erro": str(erro)
        }

    except ValueError:
        return {
            "nome": nome,
            "status": "DADOS INVALIDOS",
            "dados": None,
            "erro": "A resposta não contém JSON válido"
        }