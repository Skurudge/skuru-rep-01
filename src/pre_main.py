import re

from src.frames import transactions_csv_dict, transactions_excel_dict
from src.utils import js_loader


def choice_data() -> list[int | list[dict]]:
    """Функция запрашивает выбор пользователя об источнике из которого необходимо получить информацию о транзакциях.
    Затем функция выгружает информацию о транзакциях в соответствии с выбором пользователем источника данных.
    Затем функция запрашивает выбор пользователя о статусе транзакций по которому необходимо отфильтровать информацию
    и как итог возвращает информацию о транзакциях в соответствии с выбором пользователя о статусе транзакций"""

    print("\nПривет! Добро пожаловать в программу работы с банковскими транзакциями.")
    my_dict_choice = {
        "JSON-файл": "1. Получить информацию о транзакциях из JSON-файла",
        "CSV-файл": "2. Получить информацию о транзакциях из CSV-файла",
        "XLSX-файл": "3. Получить информацию о транзакциях из XLSX-файла",
    }
    for value in my_dict_choice.values():
        print(value)
    while True:
        my_choice_index = int(input("Выберите необходимый пункт меню: "))
        if my_choice_index in [1, 2, 3]:
            my_choice_name = list(my_dict_choice.keys())[my_choice_index - 1]
            print(f"Для обработки выбран {my_choice_name}")
            break
        else:
            match input("Выбор вне допустимого диапазона. Сделать выбор вновь? да/нет: ").lower():
                case "да":
                    continue
                case _:
                    print("Допустимый выбор не сделан. Программа сделала выбор по-умолчанию: CSV-файл")
                    my_choice_index = 2
                    break

    my_path_choice = {
        1: "E:/PythonProject/data/operations.json",
        2: "E:/PythonProject/data/transactions.csv",
        3: "E:/PythonProject/data/transactions_excel.xlsx",
    }
    my_choice_data = []
    pass_name = str(my_path_choice.get(my_choice_index))
    match my_choice_index:
        case 1:
            my_choice_data = js_loader(pass_name)
        case 2:
            my_choice_data = transactions_csv_dict(pass_name)
        case 3:
            my_choice_data = transactions_excel_dict(pass_name)
        case _:
            print("Неверный выбор")

    print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
    while True:
        my_choice_state = str(input("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: ")).upper()
        if my_choice_state in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Операции отфильтрованы по статусу {my_choice_state}")
            break
        else:
            print(f"Статус операции {my_choice_state} недоступен.")
            continue

    my_list_up = []
    pattern = re.compile(rf"{my_choice_state}")
    for item in my_choice_data:
        text = str(item.get("state"))
        match = pattern.fullmatch(text)
        if match is None:
            continue
        else:
            my_list_up.append(item)

    return [my_choice_index, my_list_up]


def filtered_sorted_data(my_list_data: list[dict], index: int) -> list[dict]:
    """Функция возвращает отсортированные и отфильтрованные данные по транзакциям в соответствии с
    вариантами выбора пользователя"""

    """block A"""
    choice_sort_date = str(input("Отсортировать операции по дате? Да/Нет/Прочее(Нет): ")).lower()
    if choice_sort_date == "да":
        choice_increase_decrease = str(
            input("Отсортировать по возрастанию или по убыванию? По возрастанию/По убыванию/Прочее(По убыванию): ")
        ).lower()
        if choice_increase_decrease == "по возрастанию":
            parameter_choice = False
        else:
            parameter_choice = True
        sorted_my_list_data = sorted(
            my_list_data, key=lambda transaction: transaction["date"], reverse=parameter_choice
        )
    else:
        sorted_my_list_data = my_list_data

    """block B"""
    choice_currency = str(input("Выводить только рублевые транзакции? Да/Нет/Прочее(Нет): ")).lower()
    if choice_currency == "да":
        match index:
            case 1:
                filtered_sorted_transactions = [
                    transaction
                    for transaction in sorted_my_list_data
                    if transaction["operationAmount"]["currency"]["code"] == "RUB"
                ]
            case _:
                filtered_sorted_transactions = [
                    transaction for transaction in sorted_my_list_data if transaction["currency_code"] == "RUB"
                ]
    else:
        filtered_sorted_transactions = sorted_my_list_data

    """block C"""
    choice_date = str(
        input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет/Прочее(Нет): ")
    ).lower()
    if choice_date == "да":
        choice_word = str(input("Введите слово для поиска: ")).lower()
        my_list_filtered = []
        pattern = re.compile(rf"{choice_word}")
        for item in filtered_sorted_transactions:
            text = str(item.get("description"))
            match = pattern.search(text, re.IGNORECASE)
            if match is None:
                continue
            else:
                my_list_filtered.append(item)
    else:
        my_list_filtered = filtered_sorted_transactions

    return my_list_filtered
