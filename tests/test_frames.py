from unittest.mock import patch

import pandas as pd
import pytest
from pandas import DataFrame

from src.frames import transactions_csv_dict, transactions_excel_dict


@pytest.fixture
def transact_data() -> DataFrame:
    sample_list_of_dict = [
        {"success": True, "query": 1, "info": 200.55, "date": "2025-01-01", "result": 20},
        {"success": False, "query": 5, "info": 502.77, "date": "2025-02-01", "result": 77},
    ]
    return pd.DataFrame(sample_list_of_dict)


def test_transactions_csv_dict(transact_data: DataFrame) -> None:
    with patch("src.frames.pd.read_csv") as mock_response:
        mock_response.return_value = transact_data
        result = transactions_csv_dict("../data/transaction.csv")
        assert result == [
            {"success": True, "query": 1, "info": 200.55, "date": "2025-01-01", "result": 20},
            {"success": False, "query": 5, "info": 502.77, "date": "2025-02-01", "result": 77},
        ]
        mock_response.assert_called_once_with("../data/transaction.csv", delimiter=";")


def test_transactions_excel_dict(transact_data: DataFrame) -> None:
    with patch("src.frames.pd.read_excel") as mock_response:
        mock_response.return_value = transact_data
        result = transactions_excel_dict("../data/transactions_excel.xlsx")
        assert result == [
            {"success": True, "query": 1, "info": 200.55, "date": "2025-01-01", "result": 20},
            {"success": False, "query": 5, "info": 502.77, "date": "2025-02-01", "result": 77},
        ]
        mock_response.assert_called_once_with("../data/transactions_excel.xlsx")
