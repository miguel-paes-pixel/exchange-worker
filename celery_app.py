from celery import Celery
import requests
from domain.services import processar_e_salvar_cotacao

app = Celery (
    "celery_app",
    broker= "amqp://guest@localhost//"
)

#TAREFA DE SALVAMENTO (SUBSCRIBER)
@app.task
def tarefa_salvar_no_txt(valor_dolar):
    #usando o código do DOMAIN
    processar_e_salvar_cotacao(valor_dolar)


#TAREFA DE BUSCA
@app.task
def buscar_cotacao():
    #busca os dados da API
    url = "https://openexchangerates.org/api/latest.json?app_id=e273224ef8bb48b4a657856c00ea6f5a"
    resposta = requests.get(url)
    dados = resposta.json()
    valor_dolar = dados ["rates"]["BRL"]

    print("--- RAIO X DOS DADOS RECEBIDOS ---")
    print(dados)
    print(f"VALOR DO DÓLAR HOJE É: R$ {valor_dolar}")
    
    tarefa_salvar_no_txt.delay(valor_dolar) # Isso envia para o RabbitMQ


#AGENDAMENTO DE BEAT (TEMPO PRA TAREFA)
app.conf.beat_schedule = {
    "buscar-dolar-a-cada-5-minutos": {
        "task" : "celery_app.buscar_cotacao",
        "schedule": 10.0,

    },
}


if __name__ == "__main__":
    print("Iniciando busca da cotação...")
    buscar_cotacao.delay()
