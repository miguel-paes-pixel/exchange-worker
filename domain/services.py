from infrastructure.repository import CotacaoRepository

def processar_e_salvar_cotacao(valor_dolar):

    if valor_dolar > 0:
        CotacaoRepository.salvar_no_txt(valor_dolar)
        print(f"✅ Sucesso! R$ {valor_dolar} registrado no arquivo histórico.")

        if valor_dolar > 6.00:
            CotacaoRepository.enviar_para_slack(valor_dolar)
            print("🚨 Alerta enviado ao Slack!")
    else:
        print("❌ Erro: Valor da cotação inválido.")