from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions: Any, curr_mod: str = "RUB") -> None:
    assert list(filter_by_currency(transactions, curr_mod)) == (
        [
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
                "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657",
            },
        ]
    )


@pytest.mark.parametrize(
    "x, y",
    [
        (
            [
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                }
            ],
            "CNY",
        ),
        ([], "RUB"),
    ],
)
def test_filter_by_currency_exc(x: Any, y: str) -> None:
    assert list(filter_by_currency(x, y)) == []


def test_transaction_description(transactions: Any) -> None:
    assert list(transaction_descriptions(transactions)) == (
        [
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод организации",
        ]
    )


@pytest.mark.parametrize(
    "value_in, value_out",
    [
        (
            [
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                }
            ],
            ["Перевод организации"],
        ),
        ([], []),
    ],
)
def test_transaction_description_exc(value_in: Any, value_out: Any) -> None:
    assert list(transaction_descriptions(value_in)) == value_out


@pytest.mark.parametrize(
    "start_number, end_number, expectation",
    [
        (
            "4573 5786 6482 1275",
            "4573 5786 6482 1280",
            [
                "4573 5786 6482 1275",
                "4573 5786 6482 1276",
                "4573 5786 6482 1277",
                "4573 5786 6482 1278",
                "4573 5786 6482 1279",
                "4573 5786 6482 1280",
            ],
        ),
        (
            "0000 0000 0000 0000",
            "0000 0000 0000 0002",
            ["0000 0000 0000 0000", "0000 0000 0000 0001", "0000 0000 0000 0002"],
        ),
        ("9999 9999 9999 9999", "9999 9999 9999 9999", ["9999 9999 9999 9999"]),
        ("600", "602", ["0000 0000 0000 0600", "0000 0000 0000 0601", "0000 0000 0000 0602"]),
        ("2", "1", []),
    ],
)
def test_card_number_generator(start_number: str, end_number: str, expectation: list) -> None:
    assert list(card_number_generator(start_number, end_number)) == expectation
