import datetime
import requests

class CotacaoRepository:
    @staticmethod
    def salvar_no_txt(valor):

        agora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        with open("historico_dolar.txt", "a") as f:
            f.write(f"[{agora}] Valor do Dólar: R$ {valor}\n")
        
    @staticmethod
    def enviar_para_slack(valor):
        url = "https://hooks.slack.com/services/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"
        payload = {"text": f"⚠️ *Alerta de Cotação* ⚠️\nO Dólar atingiu: *R$ {valor}*"}
        requests.post(url, json=payload)