import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("value, expected",
                         [(4562754852645325, '4562 75** **** 5325'),
                          (4572854658247526, '4572 85** **** 7526'),
                          ]
                         )
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize("value",
                         [12345,
                          12345678910111213141516,
                          0,
                          -100,
                          -452365745687586,
                          True,
                          [1, 'hello'],
                          {},
                          None,
                          'Underground',
                          'Правописание____',
                          '1234_GG_4565_GG_'
                          ]
                         )
def test_get_mask_card_number_type(value):
    with pytest.raises(Exception) as exc_info:
        get_mask_card_number(value)

    assert str(exc_info.value) == "Неверное значение card_number!"


@pytest.mark.parametrize("value, expected",
                         [(45627548526453257859, '**7859'),
                          (45728546582475261245, '**1245'),
                          ]
                         )
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected


@pytest.mark.parametrize("value",
                         [12345,
                          12345678910111213141516,
                          0,
                          -100,
                          -4523657456875864562,
                          True,
                          [1, 'hello'],
                          {},
                          None,
                          'Underground',
                          'Правописание____',
                          '1234_GG_4565_GG_'
                          ]
                         )
def test_get_mask_account_type(value):
    with pytest.raises(Exception) as exc_info:
        get_mask_account(value)

    assert str(exc_info.value) == "Неверное значение account!"