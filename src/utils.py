import json
import logging
import os
from pathlib import Path
from typing import Any

from src.external_api import exchange_rate

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def js_loader(path_js: str) -> Any:
    """функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    if Path(path_js).exists():
        logger.info('Run program "js_loader": file path found')
        with open(path_js, "r", encoding="utf-8") as f:
            try:
                logger.info(f'Run program "js_loader": open file {os.path.basename(path_js)}')
                datum = json.load(f)
            except json.JSONDecodeError:
                logger.error(f'Run program "js_loader": file {os.path.basename(path_js)} is empty')
                datum = []
            else:
                if type(datum) is not list:
                    logger.error('Run program "js_loader": Unused data format')
                    datum = []
    else:
        logger.error(f'Run program "js_loader": file {os.path.basename(path_js)} not found')
        datum = []
    return datum


def amount_transaction(transaction: Any) -> Any:
    """принимает на вход транзакцию и возвращает сумму транзакции в рублях
    с использованием курса конвертации при необходимости"""
    if type(transaction) is not dict or transaction == {}:
        logger.error('Run program "amount_transaction" with invalid transaction')
        raise Exception('"transaction" is not dict or empty dict')
    else:
        if "operationAmount" in list(transaction.keys()):
            if "amount" and "currency" in list(transaction.get("operationAmount").keys()):
                if "code" in list(transaction.get("operationAmount").get("currency").keys()):
                    currency_from = transaction.get("operationAmount").get("currency").get("code")
                    amount_from = transaction.get("operationAmount").get("amount")
                    logger.info(f'Run program "amount_transaction" with "exchange_rate" ( {currency_from} to RUB )')
                    amount_in_rub = exchange_rate(currency_from, "RUB", amount_from).get("result")
                    return amount_in_rub
                else:
                    logger.error('Run program "amount_transaction": transaction dict w/o "code" key')
                    raise Exception('"code" is out of keys')
            else:
                logger.error('Run program "amount_transaction": transaction dict w/o "amount" or "currency" keys')
                raise Exception('"amount" and "currency" is out of keys')
        else:
            logger.error('Run program "amount_transaction": transaction dict w/o "operationAmount" key')
            raise Exception('"operationAmount" is out of keys')
