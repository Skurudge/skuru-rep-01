import pandas as pd


def transactions_csv_dict(path_csv: str) -> list:
    """Функция для считывания финансовых операций из CSV принимает путь к файлу CSV в качестве аргумента.
    На выходе выдаёт список словарей с транзакциями."""
    transactions_csv = pd.read_csv(path_csv, delimiter=";")
    transaction_to_dict = transactions_csv.to_dict("records")
    # with open('../data/output_csv.json', 'w') as f:
    #    json.dump(transaction_to_dict, f)
    return transaction_to_dict


def transactions_excel_dict(path_excel: str) -> list:
    """Функция для считывания финансовых операций из Excel принимает путь к файлу Excel в качестве аргумента.
    На выходе выдаёт список словарей с транзакциями."""
    transactions_excel = pd.read_excel(path_excel)
    transaction_to_dict = transactions_excel.to_dict("records")
    # with open('../data/output_excel.json', 'w') as f:
    #    json.dump(transaction_to_dict, f)
    return transaction_to_dict
