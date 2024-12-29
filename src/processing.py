def filter_by_state(list_of_dicts, state_mod='EXECUTED'):
    """Функция принимает список словарей и опционально значение для ключа state, возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует опциональному значению"""
    filtered_list = []
    for item in list_of_dicts:
        if item.get('state') == state_mod:
            filtered_list.append(item)
        else:
            continue
    return filtered_list


def sort_by_date(list_of_dicts, decreasing=True):
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки словарей по дате (по умолчанию - убывание), возвращает новый список словарей, отсортированный по дате"""
    sorted_list = sorted(list_of_dicts, key=lambda x: x['date'], reverse=decreasing)
    return sorted_list