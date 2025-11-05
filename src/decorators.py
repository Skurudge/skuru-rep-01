from typing import Any, Callable


def log(filename: Any | None = None) -> Callable:
    def wrapper(function: Any) -> Callable[[tuple[Any, ...]], None]:
        def inner(*arg: Any) -> Any:
            try:
                result = function(*arg)
            except Exception as e:
                if filename is None:
                    print(f"{function.__name__} ERROR ({e}), inputs: {arg}")
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"\n{function.__name__} ERROR ({e}), inputs: {arg}")
            else:
                if filename is None:
                    print(f"{function.__name__} OK, result: {result}")
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"\n{function.__name__} OK, result: {result}")
                return result
            finally:
                if filename is None:
                    print(f"{function.__name__} STOP")
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"\n{function.__name__} STOP")

        return inner

    return wrapper


@log("mylog.txt")
def example_fun(value_1: Any, value_2: Any) -> Any:
    """Функция для тестирования декоратора №1"""
    return value_1 / (value_1 - value_2)


@log()
def example_fun_02(value_1: Any, value_2: Any) -> Any:
    """Функция для тестирования декоратора №2"""
    return value_1 / value_2
