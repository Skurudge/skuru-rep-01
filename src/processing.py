list_of_dicts = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def filter_by_state(the_list, state_mod='EXECUTED'):
    filtered_list = []
    for item in the_list:
        if item.get('state') == state_mod:
            filtered_list.append(item)
        else:
            continue
    return filtered_list

qu = filter_by_state(list_of_dicts)
glen = len(qu)
qlist = len(list_of_dicts)

print(qu)
print(glen)
print(qlist)
