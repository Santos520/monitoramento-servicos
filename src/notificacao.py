import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()


def enviar_notificacao(mensagem):
    """
    Envia uma mensagem para o Telegram.
    """

    # Obtém as credenciais do arquivo .env
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    # Verifica se as credenciais estão configuradas
    if not token or not chat_id:
        print("Credenciais do Telegram não configuradas.")
        return False

    # URL da API do Telegram
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    # Dados que serão enviados
    dados = {
        "chat_id": chat_id,
        "text": mensagem
    }

    try:
        # Envia a mensagem pela rede
        resposta = requests.post(
            url,
            json=dados,
            timeout=30
        )

        # Verifica se houve erro HTTP
        resposta.raise_for_status()

        print("Notificação enviada com sucesso!")
        return True

    except requests.exceptions.RequestException as erro:
        print(f"Erro ao enviar notificação: {erro}")
        return False