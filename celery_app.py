from celery import Celery
import requests
from infrastructure.repository import CotacaoRepository

app = Celery (
    "celery_app",
    broker= "amqp://guest@localhost//"
)

@app.task
def buscar_cotacao():
    #busca os dados da API
    url = "https://openexchangerates.org/api/latest.json?app_id=e273224ef8bb48b4a657856c00ea6f5a"
    resposta = requests.get(url)
    dados = resposta.json()
    valor_dolar = dados ["rates"]["BRL"]

    #Salva no arquivo TXT usando a camada de infraestrutura
    CotacaoRepository.salvar_no_txt(valor_dolar)
    print(f"✅ Sucesso! R$ {valor_dolar} registrado no arquivo histórico.")

    #mensagem de confirmação dos dados
    print("--- RAIO X DOS DADOS RECEBIDOS ---")
    print(dados)
    print(f"VALOR DO DÓLAR HOJE É: R$ {valor_dolar}")

#agendamento de beat (tempo pra tarefa)
app.conf.beat_schedule = {
    "buscar-dolar-a-cada-5-minutos": {
        "task" : "celery_app.buscar_cotacao",
        "schedule": 10.0,

    },
}


if __name__ == "__main__":
    print("Iniciando busca da cotação...")
    buscar_cotacao.delay()
