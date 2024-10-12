import httpx
from github_api_client import GithubApiClient
from flask import Flask, jsonify, abort


app = Flask(__name__)

@app.errorhandler(404)
def resource_not_found(error):
    return jsonify(error=str(error)), 404

@app.route("/<user>/", methods=["GET"])
def get_user(user):
    client = GithubApiClient(httpx)
    response = list_gists_for_user(client, user)
    data, status = response[0], response[1]
    if status == 404:
        abort(404, description="User not found")
    return jsonify(data)

def list_gists_for_user(client, user):
    return client.get_gists(user)


if __name__ == "__main__":
    app.run(port=8080)
