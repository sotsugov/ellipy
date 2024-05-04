import unittest
from unittest.mock import patch, Mock
from src.ellipy import get_address_info


class TestGetAddressInfo(unittest.TestCase):
    @patch("requests.get")
    def test_valid_address(self, mock_get):
        # Mock the API responses
        mock_get.side_effect = [
            Mock(status_code=200, text="1000000"),
            Mock(
                status_code=200,
                json=lambda: {
                    "total_received": 2000000,
                    "total_sent": 1000000,
                    "n_tx": 10,
                },
            ),
        ]

        address = "bc1qerf85z50plxaqmya63q60fqtdknja8k0t52njd"
        expected_info = {
            "address": address,
            "balance_btc": 0.01,
            "total_received_btc": 0.02,
            "total_sent_btc": 0.01,
            "num_transactions": 10,
        }

        result = get_address_info(address)
        self.assertEqual(result, expected_info)

    @patch("requests.get")
    def test_invalid_address(self, mock_get):
        # Mock the API response for an invalid address
        mock_get.return_value = Mock(status_code=400)

        address = "invalid_address"

        with self.assertRaises(ValueError) as context:
            get_address_info(address)

        self.assertEqual(
            str(context.exception), f"Failed to retrieve balance for address: {address}"
        )
