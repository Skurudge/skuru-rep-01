import unittest
from unittest.mock import patch

from main import main


class TestMain(unittest.TestCase):

    @patch("builtins.input")
    def test_main_1(self, mock_input_s) -> None:
        mock_input_s.side_effect = [1, "canceled", "да", "по возрастанию", "нет", "да", "карт"]

        result = main()
        expected_result = [
            {
                1: "15-07-2018 Перевод с карты на счет",
                2: "Visa Gold 9657 49** **** 2945 ->  Счет **4261",
                3: "71025 руб.",
            },
            {
                1: "08-10-2018 Перевод с карты на счет",
                2: "Visa Gold 6527 18** **** 7720 ->  Счет **9611",
                3: "77302 USD",
            },
            {
                1: "14-10-2018 Перевод с карты на счет",
                2: "Maestro 3928 54** **** 4026 ->  Счет **3493",
                3: "77751 руб.",
            },
            {
                1: "23-11-2018 Перевод с карты на карту",
                2: "Visa Gold 7305 79** **** 4042 ->  Maestro 3364 92** **** 7194",
                3: "26971 руб.",
            },
            {
                1: "17-05-2019 Перевод с карты на карту",
                2: "МИР 8021 88** **** 6544 ->  Visa Gold 8702 71** **** 3248",
                3: "74605 USD",
            },
            {
                1: "03-12-2019 Перевод с карты на карту",
                2: "MasterCard 1796 81** **** 9527 ->  Visa Classic 7699 85** **** 9288",
                3: "17628 USD",
            },
        ]

        self.assertEqual(mock_input_s.call_count, 7)
        self.assertEqual(mock_input_s.call_args_list[0][0][0], "Выберите необходимый пункт меню: ")
        self.assertEqual(
            mock_input_s.call_args_list[1][0][0], "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: "
        )
        self.assertEqual(
            mock_input_s.call_args_list[2][0][0],
            "Отсортировать операции по дате? Да/Нет/Прочее(Нет): ",
        )
        self.assertEqual(
            mock_input_s.call_args_list[3][0][0],
            "Отсортировать по возрастанию или по убыванию? По возрастанию/По убыванию/Прочее(По убыванию): ",
        )
        self.assertEqual(
            mock_input_s.call_args_list[4][0][0],
            "Выводить только рублевые транзакции? Да/Нет/Прочее(Нет): ",
        )
        self.assertEqual(
            mock_input_s.call_args_list[5][0][0],
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет/Прочее(Нет): ",
        )
        self.assertEqual(mock_input_s.call_args_list[6][0][0], "Введите слово для поиска: ")

        assert result == expected_result

    @patch("builtins.input")
    def test_main_2(self, mock_input_s) -> None:
        mock_input_s.side_effect = [2, "pending", "да", "по возрастанию", "да", "да", "вклад"]

        result = main()
        expected_result = [{1: "05-10-2020 Открытие вклада", 2: " Счет **6195", 3: "31503 Ruble"}]
        self.assertEqual(mock_input_s.call_count, 7)
        self.assertEqual(mock_input_s.call_args_list[0][0][0], "Выберите необходимый пункт меню: ")
        self.assertEqual(
            mock_input_s.call_args_list[1][0][0], "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: "
        )
        self.assertEqual(
            mock_input_s.call_args_list[2][0][0],
            "Отсортировать операции по дате? Да/Нет/Прочее(Нет): ",
        )
        self.assertEqual(
            mock_input_s.call_args_list[3][0][0],
            "Отсортировать по возрастанию или по убыванию? По возрастанию/По убыванию/Прочее(По убыванию): ",
        )
        self.assertEqual(
            mock_input_s.call_args_list[4][0][0],
            "Выводить только рублевые транзакции? Да/Нет/Прочее(Нет): ",
        )
        self.assertEqual(
            mock_input_s.call_args_list[5][0][0],
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет/Прочее(Нет): ",
        )
        self.assertEqual(mock_input_s.call_args_list[6][0][0], "Введите слово для поиска: ")

        assert result == expected_result

    @patch("builtins.input")
    def test_main_3(self, mock_input_s) -> None:
        mock_input_s.side_effect = [3, "pending", "да", "по возрастанию", "нет", "да", "орг"]

        result = main()
        expected_result = [
            {
                1: "10-05-2020 Перевод организации",
                2: "American Express 2077 16** **** 2624 ->  Счет **9313",
                3: "21170 Euro",
            },
            {
                1: "31-07-2020 Перевод организации",
                2: "Discover 5848 97** **** 1577 ->  Счет **9364",
                3: "14258 Dollar",
            },
            {1: "28-10-2020 Перевод организации", 2: "Visa 6453 53** **** 7238 ->  Счет **4978", 3: "14937 Dalasi"},
            {1: "22-11-2020 Перевод организации", 2: "n/a ->  Счет **3134", 3: "27921 Dinar"},
            {1: "10-01-2021 Перевод организации", 2: "Visa 7161 24** **** 0334 ->  Счет **6183", 3: "21117 Baht"},
            {1: "08-05-2021 Перевод организации", 2: "Discover 1256 97** **** 9173 ->  Счет **1538", 3: "16216 Euro"},
            {1: "09-05-2021 Перевод организации", 2: "Visa 4625 90** **** 8608 ->  Счет **7292", 3: "16084 Kwanza"},
            {1: "07-10-2021 Перевод организации", 2: "Discover 5138 82** **** 2482 ->  Счет **2382", 3: "14950 Pound"},
            {
                1: "27-11-2021 Перевод организации",
                2: "American Express 6477 62** **** 7562 ->  Счет **6269",
                3: "29553 Yuan Renminbi",
            },
            {1: "08-12-2021 Перевод организации", 2: "American Express 7431 98** **** 1577 ->  n/a", 3: "18989 Peso"},
            {1: "16-01-2022 Перевод организации", 2: "Visa 2627 05** **** 0658 ->  Счет **9595", 3: "16702 Pound"},
            {1: "04-04-2022 Перевод организации", 2: "n/a ->  Счет **0330", 3: "25427 Sol"},
            {1: "05-04-2022 Перевод организации", 2: "n/a ->  Счет **3869", 3: "24796 Zloty"},
            {1: "11-04-2022 Перевод организации", 2: "n/a ->  Счет **0384", 3: "11280 Ruble"},
            {
                1: "21-07-2022 Перевод организации",
                2: "American Express 3294 38** **** 1862 ->  Счет **7540",
                3: "14827 Yuan Renminbi",
            },
            {1: "27-10-2022 Перевод организации", 2: "n/a ->  Счет **2186", 3: "11180 Euro"},
            {1: "05-12-2022 Перевод организации", 2: "Visa 5505 31** **** 5497 ->  Счет **1664", 3: "19724 Peso"},
            {1: "12-02-2023 Перевод организации", 2: "n/a ->  Счет **8437", 3: "17130 Rupiah"},
            {1: "03-03-2023 Перевод организации", 2: "n/a ->  Счет **1032", 3: "21909 Dollar"},
            {1: "08-07-2023 Перевод организации", 2: "Visa 1576 85** **** 3358 ->  Счет **0320", 3: "15726 Rupiah"},
            {1: "10-07-2023 Перевод организации", 2: "n/a ->  Счет **8996", 3: "31406 Yen"},
        ]
        self.assertEqual(mock_input_s.call_count, 7)
        self.assertEqual(mock_input_s.call_args_list[0][0][0], "Выберите необходимый пункт меню: ")
        self.assertEqual(
            mock_input_s.call_args_list[1][0][0], "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: "
        )
        self.assertEqual(
            mock_input_s.call_args_list[2][0][0],
            "Отсортировать операции по дате? Да/Нет/Прочее(Нет): ",
        )
        self.assertEqual(
            mock_input_s.call_args_list[3][0][0],
            "Отсортировать по возрастанию или по убыванию? По возрастанию/По убыванию/Прочее(По убыванию): ",
        )
        self.assertEqual(
            mock_input_s.call_args_list[4][0][0],
            "Выводить только рублевые транзакции? Да/Нет/Прочее(Нет): ",
        )
        self.assertEqual(
            mock_input_s.call_args_list[5][0][0],
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет/Прочее(Нет): ",
        )
        self.assertEqual(mock_input_s.call_args_list[6][0][0], "Введите слово для поиска: ")

        assert result == expected_result
