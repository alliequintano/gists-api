# gists-api
Simple API to list a GitHub user’s public gists

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