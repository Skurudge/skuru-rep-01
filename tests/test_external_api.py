import os
from unittest.mock import Mock, patch

from dotenv import load_dotenv

from src.external_api import exchange_rate

load_dotenv()
API_KEY = os.getenv("APIKEY")


def test_exchange_rate() -> None:
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
        result = exchange_rate("USD", "RUB", 1)
        assert result == {
            "currency_from": "USD",
            "currency_to": "RUB",
            "rate": 200.55,
            "amount": 1.00,
            "result": 200.55,
        }
