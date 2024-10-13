import unittest
import os
import sys
from unittest.mock import Mock, patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../gists_api')))
from gists_api import app
from gists_api import list_gists_for_user
from github_api_client import GithubApiClient


class TestGistsApi(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_errors_return_as_json(self):
        response = self.app.get(
            "/not/a/route",
            content_type="application/json",
        )
        self.assertEqual(response.content_type, "application/json")

    @patch('github_api_client.GithubApiClient.get_gists')
    def test_no_gists(self, mock_get):
        mock_get.return_value = [], 200
        response = self.app.get(
            "/userwithnogists/",
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    @patch('github_api_client.GithubApiClient.get_gists')
    def test_user_not_found(self, mock_get):
        mock_get.return_value = {"status": "404"}, 404
        response = self.app.get(
            "/notauser/",
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"status": "404"})

    @patch('github_api_client.GithubApiClient.get_gists')
    def test_user_endpoint_exists(self, mock_get):
        mock_get.return_value = {"user": "gists"}, 200
        response = self.app.get(
            "/octocat/",
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "application/json")

    def test_user_with_data(self):
        client = Mock(
            spec_set=GithubApiClient,
            get_gists=lambda x: {"sample": "response"}
        )
        data = list_gists_for_user(client, 'octocat')
        self.assertEqual(data, {"sample": "response"})


if __name__ == '__main__':
    unittest.main()
