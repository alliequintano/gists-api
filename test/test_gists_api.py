import unittest
import os
import sys
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gists_api import get_gists

class TestGistsApi(unittest.TestCase):

    @patch('gists_api.requests.get')
    def test_get_gists_accepts_user(self, mock_get):
        mock_get.return_value.status_code = 200
        response = get_gists('octocat')
        self.assertEqual(response.status_code, 200)


    @patch('gists_api.requests.get') 
    def test_get_gists_makes_request(self, mock_get):
        mock_get.return_value.status_code = 200
        response = get_gists('octocat')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()