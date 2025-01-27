from typing import Any, Generator


def filter_by_currency(trans: Any, curr_mod: str = "USD") -> filter:
    """Принимает на вход список словарей, представляющих транзакции.
    Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""
    trans_filtered = filter(lambda x: x.get("operationAmount").get("currency").get("code") == curr_mod, trans)
    return trans_filtered


def transaction_descriptions(transact: Any) -> map:
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    description = map(lambda x: x.get("description"), transact)
    return description


def card_number_generator(start: str, stop: str) -> Generator:
    """Выдает номера банковских карт в формате 'ХХХХ ХХХХ ХХХХ XXXX', где
    X — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999, принимая на вход
    начальное и конечное значения из заданного диапазона номеров"""
    start_num_int = int(start.replace(" ", ""))
    end_num_int = int(stop.replace(" ", ""))
    while start_num_int <= end_num_int:
        if len(str(start_num_int)) == 16:
            card_num_iteration = (
                str(start_num_int)[:4]
                + " "
                + str(start_num_int)[4:8]
                + " "
                + str(start_num_int)[8:12]
                + " "
                + str(start_num_int)[12:16]
            )
        else:
            start_num_i = str(start_num_int).rjust(16, "0")
            card_num_iteration = (
                str(start_num_i)[:4]
                + " "
                + str(start_num_i)[4:8]
                + " "
                + str(start_num_i)[8:12]
                + " "
                + str(start_num_i)[12:16]
            )
        yield card_num_iteration
        start_num_int += 1
