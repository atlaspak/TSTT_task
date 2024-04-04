import unittest
import json
import sys
sys.path.append('..')
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_api_items(self):
        response = self.app.get('/api/items')
        data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

if __name__ == '__main__':
    unittest.main()
