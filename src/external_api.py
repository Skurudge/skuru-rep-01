import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("APIKEY")


def exchange_rate(curr_from: str, curr_to: str, amount: float) -> dict:
    """функция обращается к внешнему API для получения текущего курса валют
    и конвертации суммы операции в заданную валюту"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={curr_to}&from={curr_from}&amount={amount}"
    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise ValueError(f"Failed to get currency rate {curr_from}")
    data = response.json()
    return {
        "currency_from": data.get("query").get("from"),
        "currency_to": data.get("query").get("to"),
        "rate": data.get("info").get("rate"),
        "amount": data.get("query").get("amount"),
        "result": data.get("result"),
    }
