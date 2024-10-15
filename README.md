# gists-api
Simple API to list a GitHub user’s public gists. Fetches data from the GitHub API.

Note: Pagination of the GitHub API not supported yet.

## API endpoints
### User
```
GET /{user}
```
Retrieve gists for given user (e.g. `GET /octocat`).

#### Response
(Does not currently modify the response from the GitHub API, see: https://docs.github.com/en/rest/gists/gists#list-gists-for-a-user)

## Run
Build and run with Docker
```
docker build . -t gists-api
docker run --rm -p 8080:8080 gists-api
```

## Test
Create and initialize virtual environment
```
python -m venv .venv
source .venv/bin/activate
```

Install requirements
```
pip install -r requirements.txt
```

Run tests
```
python test/test_gists_api.py
```