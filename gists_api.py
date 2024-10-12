import httpx
from github_api_client import GithubApiClient


def list_gists_for_user(client, user):
    return client.get_gists(user)


def main():
    # the main will be from flask to run the api
    client = GithubApiClient(httpx)
    gists = list_gists_for_user(client, 'octocat')
    print(gists)

if __name__ == "__main__":
    main()
