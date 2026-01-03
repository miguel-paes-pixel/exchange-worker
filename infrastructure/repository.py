import datetime

class CotacaoRepository:
    @staticmethod
    def salvar_no_txt(valor):

        agora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        with open("historico_dolar.txt", "a") as f:
            f.write(f"[{agora}] Valor do Dólar: R$ {valor}\n")