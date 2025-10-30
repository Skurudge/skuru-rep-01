from unittest.mock import Mock, patch

import pytest

from src.utils import amount_transaction, js_loader


@pytest.mark.parametrize(
    "path_verification, expectation",
    [("../data/operation_0.json", []), ("../data/operations_null.json", []), ("../d/operations.json", [])],
)
def test_js_loader_exceptions(path_verification: str, expectation: list) -> None:
    assert js_loader(path_verification) == expectation


transaction_sample = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560",
}


def test_amount_transaction() -> None:
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 1},
        "info": {"timestamp": 9999999999, "rate": 200.55},
        "date": "2025-01-01",
        "result": 200.55,
    }
    with patch("requests.get", return_value=mock_response):
        repost = amount_transaction(transaction_sample)
        assert repost == 200.55
