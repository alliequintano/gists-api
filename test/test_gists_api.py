import unittest
import os
import sys
from unittest.mock import Mock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gists_api import list_gists_for_user
from github_api_client import GithubApiClient

class TestGistsApi(unittest.TestCase):

    def test_list_gists_for_user_response(self):
        client = Mock(
            spec_set=GithubApiClient,
            get_gists=lambda x: {"sample": "response"}
        )
        response = list_gists_for_user(client, 'octocat')
        self.assertEquals(response, {"sample": "response"})


if __name__ == '__main__':
    unittest.main()
