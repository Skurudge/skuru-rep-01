import pytest


@pytest.fixture
def card_number_example() -> int:
    return 7000792289606361


@pytest.fixture
def account_example() -> int:
    return 45236587452365845987


@pytest.fixture
def card_type_example() -> str:
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def account_type_example() -> str:
    return "Счет 73654108430135874305"


@pytest.fixture
def date_example() -> str:
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def list_of_dicts_example() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_of_dicts_same_date() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T08:21:33.419441"},
    ]
