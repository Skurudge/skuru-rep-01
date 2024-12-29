def filter_by_state(list_of_dicts: list[dict], state_mod: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и опционально значение для ключа state,
    возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует
    опциональному значению"""
    filtered_list = []
    for item in list_of_dicts:
        if item.get("state") == state_mod:
            filtered_list.append(item)
    return filtered_list


def sort_by_date(list_of_dicts: list[dict], decreasing: bool = True) -> list[dict]:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    словарей по дате (по умолчанию - убывание), возвращает новый список словарей, отсортированный по дате"""
    sorted_list = sorted(list_of_dicts, key=lambda x: x["date"], reverse=decreasing)
    return sorted_list
