import requests

def obter_detalhes_transacao_etherscan(api_key, transacao_hash):
    base_url = "https://api.etherscan.io/api"

    parametros = {
        "module": "proxy",
        "action": "eth_getTransactionByHash",
        "txhash": transacao_hash,
        "apikey": api_key,
    }

    resposta = requests.get(base_url, params=parametros)
    dados = resposta.json()

    if "result" in dados and dados["result"] is not None:
        result = dados["result"]
        destinatario = result["to"]
        valor_wei = int(result["value"], 16)
        valor_eth = valor_wei / 10**18

        print("Detalhes da Transação:")
        print(f"Hash: {transacao_hash}")
        print(f"Destinatário: {destinatario}")
        print(f"Valor: {valor_eth} Ether")
    else:
        print("Transação não encontrada ou erro na requisição.")

# Substitua 'SUA_CHAVE_DE_API_AQUI' pela sua chave de API da Etherscan
api_key = 'X9JUBW77R5VPMN9AGKEHHIY3GAMB2IUYDA'
# Substitua 'HASH_DA_TRANSACAO_AQUI' pelo hash da transação que você deseja verificar
transacao_hash = '0xbcc48269a0caa77f0f0c12fa4bc69737764d3f07171d82697f1a57660ac96134'

obter_detalhes_transacao_etherscan(api_key, transacao_hash)