import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_fixture(list_of_dicts_example: list[dict]) -> None:
    assert filter_by_state(list_of_dicts_example) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (
            [
                {"id": 41428829, "state": "FIXED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "FIXED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "FIXED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "FIXED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
            [{"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}],
        ),
        (
            [
                {"id": 41428829, "state": "FIXED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "FIXED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "FIXED",
            [
                {"id": 41428829, "state": "FIXED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "FIXED", "date": "2018-09-12T21:27:25.241689"},
            ],
        ),
    ],
)
def test_filter_by_state(x: list[dict], y: str, expected: list[dict]) -> None:
    assert filter_by_state(x, y) == expected


def test_filter_by_state_except(list_of_dicts_example: list[dict], state_mod: str = "FIXED") -> None:
    with pytest.raises(Exception) as exc_info:
        filter_by_state(list_of_dicts_example, state_mod)

    assert str(exc_info.value) == f"Словари со статусом {state_mod} отсутствуют в списке"


def test_sort_by_date_fixture(list_of_dicts_example: list[dict]) -> None:
    assert sort_by_date(list_of_dicts_example) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert sort_by_date(list_of_dicts_example, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_same_date(list_of_dicts_same_date: list[dict]) -> None:
    assert sort_by_date(list_of_dicts_same_date) == [
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T08:21:33.419441"},
    ]
    assert sort_by_date(list_of_dicts_same_date, False) == [
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
    ]


@pytest.mark.parametrize(
    "value",
    [
        0,
        -357,
        False,
        [],
        {},
        None,
        "",
        [
            {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T08:21:33.419441"},
            {"id": 41428829, "state": "EXECUTED"},
        ],
        [
            {"id": 615064591, "state": "CANCELED", "date": "2019-419441"},
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        ],
    ],
)
def test_sort_by_date_except(value: list[dict]) -> None:
    with pytest.raises(Exception) as exc_info:
        sort_by_date(value)

    assert (
        str(exc_info.value)
        == "Список словарей не корректен, значение даты отсутствует/ не соответствует заданному формату!"
    )
