import httpx
from github_api_client import GithubApiClient
from flask import Flask, jsonify, json
from werkzeug.exceptions import HTTPException


app = Flask(__name__)

@app.errorhandler(HTTPException)
def handle_exception(error):
    response = error.get_response()
    response.data = json.dumps({
        "code": error.code,
        "name": error.name,
        "description": error.description,
    })
    response.content_type = "application/json"
    return response

@app.route("/<user>/", methods=["GET"])
def get_user(user):
    client = GithubApiClient(httpx)
    response = list_gists_for_user(client, user)
    data, status = response[0], response[1]
    return jsonify(data), status

def list_gists_for_user(client, user):
    return client.get_gists(user)


if __name__ == "__main__":
    app.run(port=8080, host='0.0.0.0')
