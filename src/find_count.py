import re
from collections import Counter


def transaction_bank_search(my_transaction_list: list[dict], my_search: str) -> list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска, а возвращает
    список словарей, у которых в описании есть данная строка."""
    my_transaction_search = []
    pattern = re.compile(rf"{my_search}")
    for item in my_transaction_list:
        text = str(item.get("description"))
        match = pattern.fullmatch(text)
        if match is None:
            continue
        else:
            my_transaction_search.append(item)
    return my_transaction_search


def transaction_bank_group(my_transaction_list: list[dict], my_group_list: list[str]) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории."""
    new_transaction_list = []
    for item in my_transaction_list:
        my_group = item.get("description")
        new_transaction_list.append(my_group)
    group_transaction_list = Counter(new_transaction_list)
    my_group_dict = {k: group_transaction_list[k] for k in group_transaction_list if k in my_group_list}
    return my_group_dict
