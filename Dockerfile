FROM python:3.9-alpine

RUN mkdir /app

COPY gists_api.py github_api_client.py requirements.txt /app/

RUN pip install -r /app/requirements.txt

EXPOSE 8080

CMD [ "python", "./app/gists_api.py" ]
