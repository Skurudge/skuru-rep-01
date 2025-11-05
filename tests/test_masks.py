import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_fixture(card_number_example: int) -> None:
    assert get_mask_card_number(card_number_example) == "7000 79** **** 6361"


@pytest.mark.parametrize(
    "value, expected",
    [
        (4562754852645325, "4562 75** **** 5325"),
        (4572854658247526, "4572 85** **** 7526"),
    ],
)
def test_get_mask_card_number(value: int, expected: str) -> None:
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize(
    "value",
    [
        12345,
        12345678910111213141516,
        0,
        -100,
        -452365745687586,
        True,
        [1, "hello"],
        {},
        None,
        "Underground",
        "Правописание____",
        "1234_GG_4565_GG_",
    ],
)
def test_get_mask_card_number_except(value: int | bool | list[int | str] | dict | None | str) -> None:
    with pytest.raises(Exception) as exc_info:
        get_mask_card_number(value)

    assert str(exc_info.value) == "Неверное значение card_number!"


def test_get_mask_account_fixture(account_example: int) -> None:
    assert get_mask_account(account_example) == "**5987"


@pytest.mark.parametrize(
    "value, expected",
    [
        (45627548526453257859, "**7859"),
        (45728546582475261245, "**1245"),
    ],
)
def test_get_mask_account(value: int, expected: str) -> None:
    assert get_mask_account(value) == expected


@pytest.mark.parametrize(
    "value",
    [
        12345,
        12345678910111213141516,
        0,
        -100,
        -4523657456875864562,
        True,
        [1, "hello"],
        {},
        None,
        "Underground",
        "Правописание____",
        "1234_GG_4565_GG_",
    ],
)
def test_get_mask_account_except(value: int | bool | list[int | str] | dict | None | str) -> None:
    with pytest.raises(Exception) as exc_info:
        get_mask_account(value)

    assert str(exc_info.value) == "Неверное значение account!"
