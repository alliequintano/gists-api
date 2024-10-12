class GithubApiClient:

    def __init__(self, client):
        self._client = client

    def get_gists(self, user):
        return self._client.get(
             f"https://api.github.com/users/{user}/gists"
        ).json()
