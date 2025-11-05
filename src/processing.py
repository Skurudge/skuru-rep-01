from collections.abc import Sized


def filter_by_state(list_of_dicts: list[dict], state_mod: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и опционально значение для ключа state,
    возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует
    опциональному значению"""
    filtered_list = []
    for item in list_of_dicts:
        if item.get("state") == state_mod:
            filtered_list.append(item)
    if not filtered_list:
        raise Exception(f"Словари со статусом {state_mod} отсутствуют в списке")
    else:
        return filtered_list


def sort_by_date(list_of_dicts: list | Sized | None, decreasing: bool = True) -> list[dict]:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    словарей по дате (по умолчанию - убывание), возвращает новый список словарей, отсортированный по дате"""
    if type(list_of_dicts) is not list or list_of_dicts == [] or list_of_dicts is None:
        raise Exception("Список словарей не корректен, значение даты отсутствует/ не соответствует заданному формату!")
    else:
        i = 0
        for item in list_of_dicts:
            if item.get("date") is None:
                continue
            else:
                if len(item.get("date")) == 26:
                    i += 1
        if len(list_of_dicts) != i:
            raise Exception(
                "Список словарей не корректен, значение даты отсутствует/ не соответствует заданному формату!"
            )
        else:
            sorted_list = sorted(list_of_dicts, key=lambda x: x["date"], reverse=decreasing)
            return sorted_list
