from datetime import datetime

from src.pre_main import choice_data, filtered_sorted_data
from src.widget import mask_account_card


def main() -> list[dict]:
    """Функция отвечает за основную логику проекта и связывает функциональности между собой"""

    output = choice_data()
    index_choice = int(output[0])
    list_choice = list(output[1])
    result = filtered_sorted_data(list_choice, index_choice)

    print("\nРаспечатываю итоговый список транзакций...")

    count_operations = len(result)
    if count_operations == 0:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"\nВсего банковских операций в выборке: {count_operations}\n")

    # создаем словарь с результатом

    my_aimed_list = []

    for item in result:

        original_date = item.get("date")
        original_description = item.get("description")

        match index_choice:
            case 1:
                parsed_date = datetime.strptime(original_date, "%Y-%m-%dT%H:%M:%S.%f")
                original_amount = float(item.get("operationAmount").get("amount"))
                original_currency = item.get("operationAmount").get("currency").get("name")

                try:
                    masked_from = mask_account_card(item.get("from")) + " -> "
                except Exception:
                    masked_from = ""

                try:
                    masked_to = mask_account_card(item.get("to"))
                except Exception:
                    masked_to = ""

            case _:
                parsed_date = datetime.strptime(original_date, "%Y-%m-%dT%H:%M:%SZ")
                original_amount = float(item.get("amount"))
                original_currency = item.get("currency_name")

                if type(item.get("from")).__name__ != "str":
                    masked_from = ""
                else:
                    try:
                        masked_from = mask_account_card(item.get("from")) + " -> "
                    except Exception:
                        masked_from = "n/a -> "

                if type(item.get("to")).__name__ != "str":
                    masked_to = ""
                else:
                    try:
                        masked_to = mask_account_card(item.get("to"))
                    except Exception:
                        masked_to = "n/a"

        formatted_date = parsed_date.strftime("%d-%m-%Y")
        round_amount = int(round(original_amount, 0))

        # создаем удобный словарь как результат и для печати

        item_dict = {
            1: f"{formatted_date} {original_description}",
            2: f"{masked_from} {masked_to}",
            3: f"{round_amount} {original_currency}",
        }

        my_aimed_list.append(item_dict)

    for item in my_aimed_list:
        for value in item.values():
            print(f"{value}")
        print()

    return my_aimed_list
