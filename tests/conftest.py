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
