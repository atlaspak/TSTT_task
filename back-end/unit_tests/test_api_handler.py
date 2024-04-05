import unittest
from unittest.mock import MagicMock
from flask import Flask
import sys

sys.path.append('..')
from app import APIHandler  

class TestAPIHandler(unittest.TestCase):
    def setUp(self):
        app = Flask(__name__)
        app.testing = True
        self.app = app.test_client()

        # User mock for data manager
        self.mock_data_manager = MagicMock()
        self.api_handler = APIHandler(self.mock_data_manager)

        with app.app_context():
            app.add_url_rule('/api/items', view_func=self.api_handler.get_items)
            app.add_url_rule('/api/summary', view_func=self.api_handler.get_summary)

    def test_get_items(self):
        mock_data = [
            {"scenario": "Mock Scenario 1", "config": "Mock Config A"},
            {"scenario": "Mock Scenario 2", "config": "Mock Config B"}
        ]
        self.mock_data_manager.get_data.return_value = mock_data

        response = self.app.get('/api/items')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, mock_data)

    def test_get_summary(self):
        mock_summary = {
            "total_scenarios": 2,
            "statuses": {"pass": 1, "fail": 1, "busy": 0, "wait": 0}
        }
        self.mock_data_manager.get_summary.return_value = mock_summary

        response = self.app.get('/api/summary')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, mock_summary)

if __name__ == '__main__':
    unittest.main()