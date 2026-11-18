
import schedule
import time
import sys
import logging

from datetime import datetime
from monitor import verificar_servico, verificar_json
from notificacao import enviar_notificacao


# Configuração dos arquivos de log
logging.basicConfig(
    filename="monitoramento.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


# Guarda o último estado conhecido de cada serviço
estado_anterior = {}


def executar_monitoramento():

    print("=" * 50)
    print("MONITORAMENTO DE SERVIÇOS")
    print("=" * 50)

    horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    logging.info("Iniciando monitoramento de serviços")

    # Serviços que serão monitorados
    servicos = [
        {
            "nome": "HTTPBin",
            "url": "https://httpbin.org/status/200"
        },
        {
            "nome": "JSONPlaceholder",
            "url": "https://jsonplaceholder.typicode.com/posts/1"
        }
    ]

    resultados = []

    # Verifica os serviços
    for servico in servicos:

        resultado = verificar_servico(
            servico["nome"],
            servico["url"]
        )

        resultados.append(resultado)

    print("\nVerificação de JSON:")

    resultado_json = verificar_json(
        "JSONPlaceholder",
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    resultados.append(resultado_json)

    alertas = []

    # Analisa os resultados e identifica mudanças
    for resultado in resultados:

        nome = resultado.get("nome", "Serviço")
        status = resultado.get("status", "DESCONHECIDO")

        chave = nome

        # Diferencia a verificação HTTP da verificação JSON
        if "dados" in resultado:
            chave = nome + " - JSON"

        print(resultado)

        logging.info("Resultado: %s", resultado)

        estado = estado_anterior.get(chave)

        # Primeira verificação
        if estado is None:

            if status == "OFFLINE":
                alertas.append(
                    f"⚠️ {chave} está OFFLINE!"
                )

        # Verifica se houve mudança de status
        elif estado != status:

            if status == "OFFLINE":
                alertas.append(
                    f"🚨 ALERTA: {chave} ficou OFFLINE!"
                )

            elif status == "ONLINE":
                alertas.append(
                    f"✅ RECUPERAÇÃO: {chave} voltou a ficar ONLINE!"
                )

        # Atualiza o estado do serviço
        estado_anterior[chave] = status

    # Envia notificações somente quando houver alertas
    if alertas:

        mensagem = "📊 ALERTA DE MONITORAMENTO\n"
        mensagem += f"Horário: {horario}\n\n"

        for alerta in alertas:
            mensagem += alerta + "\n"

        enviado = enviar_notificacao(mensagem)

        if enviado:
            logging.info("Alertas enviados ao Telegram")
        else:
            logging.warning("Falha ao enviar alertas")

    else:

        print("\nNenhuma mudança de status detectada.")

        logging.info(
            "Nenhuma mudança de status detectada"
        )

    logging.info("Monitoramento finalizado")

    print("\nMonitoramento finalizado!")
    print("=" * 50)


if __name__ == "__main__":

    if "--once" in sys.argv:

        executar_monitoramento()

    else:

        print("Monitoramento automático iniciado!")

        schedule.every(5).minutes.do(
            executar_monitoramento
        )

        executar_monitoramento()

        while True:
            schedule.run_pending()
            time.sleep(1)
