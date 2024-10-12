import unittest
import os
import sys
from unittest.mock import Mock, patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gists_api import app
from gists_api import list_gists_for_user
from gists_api import get_user
from github_api_client import GithubApiClient

class TestGistsApi(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    @patch('github_api_client.GithubApiClient.get_gists')
    def test_user_endpoint_200(self, mock_get):
        mock_get.return_value = {"user": "gists"}
        response = self.app.get(
            "/octocat/",
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

    def test_user_with_data(self):
        client = Mock(
            spec_set=GithubApiClient,
            get_gists=lambda x: {"sample": "response"}
        )
        data = list_gists_for_user(client, 'octocat')
        self.assertEqual(data, {"sample": "response"})


if __name__ == '__main__':
    unittest.main()
