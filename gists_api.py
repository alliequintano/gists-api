import httpx
from github_api_client import GithubApiClient
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/<user>/", methods=["GET"])
def get_user(user):
    client = GithubApiClient(httpx)
    return jsonify(list_gists_for_user(client, user))

def list_gists_for_user(client, user):
    return client.get_gists(user)


if __name__ == "__main__":
    app.run(port=8080)
