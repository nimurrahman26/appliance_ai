import requests

def get_usd_bdt():
    try:
        url = "https://open.er-api.com/v6/latest/USD"
        data = requests.get(url).json()
        return data["rates"]["BDT"]
    except:
        return 120


def get_oil_price():
    return 85