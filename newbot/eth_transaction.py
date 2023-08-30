import requests
import eth_price

def verificar_transacao_etherscan(transacao_hash, valor_plano, carteira_destino):
    api_key = 'X9JUBW77R5VPMN9AGKEHHIY3GAMB2IUYDA'
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
        valor_wei = int(result["value"], 16)
        valor_eth = valor_wei / 10**18

        if valor_eth == valor_plano and result["to"].lower() == carteira_destino.lower():
            return "Transação confirmada e verificada."
        else:
            return "Transação confirmada, mas o valor ou destinatário não correspondem."
    else:
        return "Transação não encontrada ou erro na requisição."

# Substitua 'HASH_DA_TRANSACAO_AQUI' pelo hash da transação que você deseja verificar
transacao_hash = '0x37fc1c671b7292be6da2f20ca07682a2b4f6d3a6c148b4cc59f00e0cc5ce3ebb'
valor_plano = 15 / eth_price.eth_price  # Adjust the value accordingly
carteira_destino = "0x03fC32a7893487475617BeCF95A05813805b1D64"

status = verificar_transacao_etherscan(transacao_hash, valor_plano, carteira_destino)
print(status)

