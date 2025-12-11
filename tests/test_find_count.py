import pytest

from src.find_count import transaction_bank_group, transaction_bank_search


@pytest.fixture
def transact_sample() -> list[dict]:
    sample_list_of_dict = [
        {
            "success": True,
            "query": 1,
            "info": 200.55,
            "date": "2025-01-01",
            "result": 20,
            "description": "Перевод со счета на счет",
        },
        {
            "success": False,
            "query": 5,
            "info": 502.77,
            "date": "2025-02-01",
            "result": 77,
            "description": "Открытие вклада",
        },
        {"success": True, "query": 3, "info": 1000.75, "date": "2025-03-01", "result": 90, "description": "Прочее"},
        {
            "success": True,
            "query": 2,
            "info": 25.42,
            "date": "2025-04-01",
            "result": 55,
            "description": "Перевод со счета на счет",
        },
        {"success": False, "query": 7, "info": 52.99, "date": "2025-05-01", "result": 31, "description": "Прочее"},
    ]
    return sample_list_of_dict


@pytest.fixture
def my_string_search() -> str:
    sample_string = "Перевод со счета на счет"
    return sample_string


@pytest.fixture
def my_list_search() -> list[str]:
    sample_list = ["Открытие вклада", "Перевод со счета на счет", "Другое"]
    return sample_list


def test_transaction_bank_search(transact_sample: list[dict], my_string_search: str) -> None:
    result = transaction_bank_search(transact_sample, my_string_search)
    assert result == [
        {
            "success": True,
            "query": 1,
            "info": 200.55,
            "date": "2025-01-01",
            "result": 20,
            "description": "Перевод со счета на счет",
        },
        {
            "success": True,
            "query": 2,
            "info": 25.42,
            "date": "2025-04-01",
            "result": 55,
            "description": "Перевод со счета на счет",
        },
    ]


def test_transaction_bank_group(transact_sample: list[dict], my_list_search: list[str]) -> None:
    result = transaction_bank_group(transact_sample, my_list_search)
    assert result == {"Открытие вклада": 1, "Перевод со счета на счет": 2}


def test_transaction_bank_search_empty(transact_sample: list[dict]) -> None:
    result = transaction_bank_search(transact_sample, "")
    assert result == []


def test_transaction_bank_group_empty(transact_sample: list[dict]) -> None:
    result = transaction_bank_group(transact_sample, [])
    assert result == {}
