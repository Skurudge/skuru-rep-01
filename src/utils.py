import json
from pathlib import Path
from typing import Any

from src.external_api import exchange_rate


def js_loader(path_js: str) -> Any:
    """функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    datum = []
    if Path(path_js).exists():
        with open(path_js, "r", encoding="utf-8") as f:
            try:
                datum = json.load(f)
            except json.JSONDecodeError:
                datum = []
            else:
                if type(datum) is not list:
                    datum = []
    return datum


def amount_transaction(transaction: Any) -> Any:
    """принимает на вход транзакцию и возвращает сумму транзакции в рублях
    c использованием курса конвертации при необходимости"""
    currency_from = transaction.get("operationAmount").get("currency").get("code")
    amount_from = transaction.get("operationAmount").get("amount")
    amount_in_rub = exchange_rate(currency_from, "RUB", amount_from).get("result")
    return amount_in_rub
