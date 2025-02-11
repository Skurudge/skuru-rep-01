import pytest
from _pytest.capture import CaptureFixture

from src.decorators import example_fun, example_fun_02


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (5, 3, "example_fun OK, result: 2.5"),
        (3, 3, "example_fun ERROR (division by zero), inputs: (3, 3)"),
        (4, 2, "example_fun OK, result: 2.0"),
    ],
)
def test_log(x: int, y: int, expected: str) -> None:
    example_fun(x, y)
    list_of_lines = []
    with open("mylog.txt", "r") as file:
        for line in file:
            list_of_lines.append(line[:-1])
    if expected in list_of_lines[-6:]:
        assert True
    else:
        assert False


def test_log_next_one(capsys: CaptureFixture[str]) -> None:
    example_fun_02(5, 2)
    captured = capsys.readouterr()
    assert captured.out == "example_fun_02 OK, result: 2.5\nexample_fun_02 STOP\n"


def test_log_next_two(capsys: CaptureFixture[str]) -> None:
    example_fun_02(5, 0)
    captured = capsys.readouterr()
    assert captured.out == "example_fun_02 ERROR (division by zero), inputs: (5, 0)\nexample_fun_02 STOP\n"
