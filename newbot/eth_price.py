import requests

def get_eth_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "ethereum",
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "ethereum" in data and "usd" in data["ethereum"]:
        eth_price = data["ethereum"]["usd"]
        return eth_price
    else:
        return None

# Get the current ETH price
eth_price = get_eth_price()

if eth_price is not None:
    print(f"Current ETH price: ${eth_price}")
else:
    print("Failed to fetch ETH price.")