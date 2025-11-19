import unittest
from unittest.mock import patch

from src.pre_main import choice_data, filtered_sorted_data


class TestPreMain(unittest.TestCase):

    @patch("builtins.input")
    def test_choice_data(self, mock_input) -> None:
        mock_input.side_effect = [7, "да", 1, "canceled"]

        result = choice_data()[1]
        expected_result = [
            {
                "date": "2018-09-12T21:27:25.241689",
                "description": "Перевод организации",
                "from": "Visa Platinum 1246377376343588",
                "id": 594226727,
                "operationAmount": {"amount": "67314.70", "currency": {"code": "RUB", "name": "руб."}},
                "state": "CANCELED",
                "to": "Счет 14211924144426031657",
            },
            {
                "date": "2018-10-14T08:21:33.419441",
                "description": "Перевод с карты на счет",
                "from": "Maestro 3928549031574026",
                "id": 615064591,
                "operationAmount": {"amount": "77751.04", "currency": {"code": "RUB", "name": "руб."}},
                "state": "CANCELED",
                "to": "Счет 84163357546688983493",
            },
            {
                "date": "2018-11-23T17:47:33.127140",
                "description": "Перевод с карты на карту",
                "from": "Visa Gold 7305799447374042",
                "id": 476991061,
                "operationAmount": {"amount": "26971.25", "currency": {"code": "RUB", "name": "руб."}},
                "state": "CANCELED",
                "to": "Maestro 3364923093037194",
            },
            {
                "date": "2019-01-15T17:58:27.064377",
                "description": "Перевод организации",
                "from": "Visa Platinum 2241653116508487",
                "id": 970724427,
                "operationAmount": {"amount": "90688.44", "currency": {"code": "USD", "name": "USD"}},
                "state": "CANCELED",
                "to": "Счет 26494285169417058486",
            },
            {
                "date": "2018-10-08T09:05:05.282282",
                "description": "Перевод с карты на счет",
                "from": "Visa Gold 6527183396477720",
                "id": 608117766,
                "operationAmount": {"amount": "77302.31", "currency": {"code": "USD", "name": "USD"}},
                "state": "CANCELED",
                "to": "Счет 38573816654581789611",
            },
            {
                "date": "2018-07-15T18:44:13.346362",
                "description": "Перевод с карты на счет",
                "from": "Visa Gold 9657499677062945",
                "id": 464419177,
                "operationAmount": {"amount": "71024.64", "currency": {"code": "RUB", "name": "руб."}},
                "state": "CANCELED",
                "to": "Счет 19213886662094884261",
            },
            {
                "date": "2019-12-03T04:27:03.427014",
                "description": "Перевод с карты на карту",
                "from": "MasterCard 1796816785869527",
                "id": 560813069,
                "operationAmount": {"amount": "17628.50", "currency": {"code": "USD", "name": "USD"}},
                "state": "CANCELED",
                "to": "Visa Classic 7699855375169288",
            },
            {
                "date": "2019-05-17T01:50:00.166954",
                "description": "Перевод с карты на карту",
                "from": "МИР 8021883699486544",
                "id": 556488059,
                "operationAmount": {"amount": "74604.56", "currency": {"code": "USD", "name": "USD"}},
                "state": "CANCELED",
                "to": "Visa Gold 8702717057933248",
            },
            {
                "date": "2019-02-14T17:38:09.910336",
                "description": "Перевод организации",
                "from": "Visa Classic 4610247282706784",
                "id": 692008409,
                "operationAmount": {"amount": "37044.95", "currency": {"code": "RUB", "name": "руб."}},
                "state": "CANCELED",
                "to": "Счет 63229171188548882700",
            },
            {
                "date": "2019-04-18T11:22:18.800453",
                "description": "Открытие вклада",
                "id": 176798279,
                "operationAmount": {"amount": "73778.48", "currency": {"code": "RUB", "name": "руб."}},
                "state": "CANCELED",
                "to": "Счет 90417871337969064865",
            },
            {
                "date": "2018-02-13T04:43:11.374324",
                "description": "Перевод организации",
                "from": "Счет 33355011456314142963",
                "id": 200634844,
                "operationAmount": {"amount": "42210.20", "currency": {"code": "RUB", "name": "руб."}},
                "state": "CANCELED",
                "to": "Счет 45735917297559088682",
            },
            {
                "date": "2018-08-17T03:57:28.607101",
                "description": "Перевод организации",
                "from": "Maestro 1913883747791351",
                "id": 710136990,
                "operationAmount": {"amount": "66906.45", "currency": {"code": "USD", "name": "USD"}},
                "state": "CANCELED",
                "to": "Счет 11492155674319392427",
            },
            {
                "date": "2018-06-08T16:14:59.936274",
                "description": "Перевод организации",
                "from": "Maestro 7552745726849311",
                "id": 121646999,
                "operationAmount": {"amount": "91121.62", "currency": {"code": "RUB", "name": "руб."}},
                "state": "CANCELED",
                "to": "Счет 34799481846914116850",
            },
            {
                "date": "2018-06-24T00:46:32.422648",
                "description": "Перевод организации",
                "from": "МИР 6381702861749111",
                "id": 816266176,
                "operationAmount": {"amount": "60030.73", "currency": {"code": "USD", "name": "USD"}},
                "state": "CANCELED",
                "to": "Счет 27804394774631586026",
            },
            {
                "date": "2018-12-24T20:16:18.819037",
                "description": "Перевод со счета на счет",
                "from": "Счет 71687416928274675290",
                "id": 27192367,
                "operationAmount": {"amount": "991.49", "currency": {"code": "RUB", "name": "руб."}},
                "state": "CANCELED",
                "to": "Счет 87448526688763159781",
            },
        ]

        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_input.call_args_list[0][0][0], "Выберите необходимый пункт меню: ")
        self.assertEqual(
            mock_input.call_args_list[1][0][0], "Выбор вне допустимого диапазона. Сделать выбор вновь? да/нет: "
        )
        self.assertEqual(mock_input.call_args_list[2][0][0], "Выберите необходимый пункт меню: ")
        self.assertEqual(
            mock_input.call_args_list[3][0][0], "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: "
        )

        assert result == expected_result

    @patch("builtins.input")
    def test_filtered_sorted_data_1(self, mock_input_s) -> None:
        mock_input_s.side_effect = [7, "да", 3, "pending", "да", "по возрастанию", "нет", "да", "счет"]

        output = choice_data()
        index_choice = output[0]
        list_choice = output[1]
        result = filtered_sorted_data(list_choice, index_choice)
        expected_result = [
            {
                "id": 1065726.0,
                "state": "PENDING",
                "date": "2020-07-02T04:46:11Z",
                "amount": 29169.0,
                "currency_name": "Shilling",
                "currency_code": "UGX",
                "from": "Счет 02128618384427301635",
                "to": "Счет 25745812541257778590",
                "description": "Перевод со счета на счет",
            },
            {
                "id": 2504828.0,
                "state": "PENDING",
                "date": "2021-03-22T05:59:14Z",
                "amount": 11982.0,
                "currency_name": "Rupiah",
                "currency_code": "IDR",
                "from": "Счет 40357013384457231147",
                "to": "Счет 59361600183832821416",
                "description": "Перевод со счета на счет",
            },
            {
                "id": 3530319.0,
                "state": "PENDING",
                "date": "2022-02-08T18:49:18Z",
                "amount": 11294.0,
                "currency_name": "Pound",
                "currency_code": "SYP",
                "from": "Счет 64339097692172543801",
                "to": "Счет 65515023539147659794",
                "description": "Перевод со счета на счет",
            },
            {
                "id": 4492444.0,
                "state": "PENDING",
                "date": "2022-09-13T02:41:12Z",
                "amount": 13086.0,
                "currency_name": "Dollar",
                "currency_code": "CAD",
                "from": "Счет 07318089075038053901",
                "to": "Счет 05172516288862953128",
                "description": "Перевод со счета на счет",
            },
            {
                "id": 5170766.0,
                "state": "PENDING",
                "date": "2023-01-11T18:41:24Z",
                "amount": 15534.0,
                "currency_name": "Quetzal",
                "currency_code": "GTQ",
                "from": "Счет 91269211633331489581",
                "to": "Счет 83962090923263746792",
                "description": "Перевод со счета на счет",
            },
            {
                "id": 2449358.0,
                "state": "PENDING",
                "date": "2023-03-21T15:22:20Z",
                "amount": 28671.0,
                "currency_name": "Hryvnia",
                "currency_code": "UAH",
                "from": "Счет 09503816595143782708",
                "to": "Счет 88842829646860865403",
                "description": "Перевод со счета на счет",
            },
            {
                "id": 2258909.0,
                "state": "PENDING",
                "date": "2023-06-05T00:33:41Z",
                "amount": 27030.0,
                "currency_name": "Rand",
                "currency_code": "ZAR",
                "from": "Счет 95883985429884067440",
                "to": "Счет 98017798502227556609",
                "description": "Перевод со счета на счет",
            },
            {
                "id": 2236163.0,
                "state": "PENDING",
                "date": "2023-06-29T20:33:57Z",
                "amount": 19612.0,
                "currency_name": "Peso",
                "currency_code": "PHP",
                "from": "Счет 40742441133364006255",
                "to": "Счет 52562367063354770261",
                "description": "Перевод со счета на счет",
            },
            {
                "id": 1999804.0,
                "state": "PENDING",
                "date": "2023-10-28T11:17:31Z",
                "amount": 34455.0,
                "currency_name": "Hryvnia",
                "currency_code": "UAH",
                "from": "Счет 42109207415591580635",
                "to": "Счет 74058089109726743250",
                "description": "Перевод со счета на счет",
            },
        ]

        self.assertEqual(mock_input_s.call_count, 9)
        self.assertEqual(mock_input_s.call_args_list[0][0][0], "Выберите необходимый пункт меню: ")
        self.assertEqual(
            mock_input_s.call_args_list[1][0][0], "Выбор вне допустимого диапазона. Сделать выбор вновь? да/нет: "
        )
        self.assertEqual(mock_input_s.call_args_list[2][0][0], "Выберите необходимый пункт меню: ")
        self.assertEqual(
            mock_input_s.call_args_list[3][0][0], "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: "
        )

        self.assertEqual(
            mock_input_s.call_args_list[4][0][0],
            "Отсортировать операции по дате? Да/Нет/Прочее(Нет): ",
        )
        self.assertEqual(
            mock_input_s.call_args_list[5][0][0],
            "Отсортировать по возрастанию или по убыванию? По возрастанию/По убыванию/Прочее(По убыванию): ",
        )
        self.assertEqual(
            mock_input_s.call_args_list[6][0][0],
            "Выводить только рублевые транзакции? Да/Нет/Прочее(Нет): ",
        )
        self.assertEqual(
            mock_input_s.call_args_list[7][0][0],
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет/Прочее(Нет): ",
        )
        self.assertEqual(mock_input_s.call_args_list[8][0][0], "Введите слово для поиска: ")

        assert result == expected_result
