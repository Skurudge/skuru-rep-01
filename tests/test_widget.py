import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card_fixture(card_type_example: str) -> None:
    assert mask_account_card(card_type_example) == "Visa Platinum 7000 79** **** 6361"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(value: str, expected: str) -> None:
    assert mask_account_card(value) == expected


@pytest.mark.parametrize(
    "value",
    [
        1234567891011121221121213141516,
        0,
        -357,
        False,
        [1, "hello"],
        {},
        None,
        "",
        "Счет 5999414228426353",
        "Visa Platinum 73654108430135874305",
    ],
)
def test_mask_account_card_except(value: int | bool | list[int | str] | dict | None | str) -> None:
    with pytest.raises(Exception) as exc_info:
        mask_account_card(value)

    assert str(exc_info.value) == "Неверное значение на входе функции!"


def test_get_date_fixture(date_example: str) -> None:
    assert get_date(date_example) == "11.03.2024"


@pytest.mark.parametrize(
    "value",
    [
        123456,
        0,
        -357,
        False,
        [1, "hello"],
        {},
        None,
        "",
        "2024-36-11T02:26:18.671407",
        "2024-03-99T02:26:18.671407",
        "2024-03-11T02:26:18.671407ABC",
        "2024-03-11T02:26",
    ],
)
def test_get_date_except(value: int | bool | list[int | str] | dict | None | str) -> None:
    with pytest.raises(Exception) as exc_info:
        get_date(value)

    assert str(exc_info.value) == "Значение на входе не соответствует заданному формату даты!"
