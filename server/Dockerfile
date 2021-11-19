FROM python:3.8.5-slim

RUN apt-get update && apt-get install -y postgresql libpq-dev install gcc psycopg2-binary python3-psycopg2
RUN mkdir /server
WORKDIR /server

COPY ./server/pyproject.toml /server/
COPY ./server/poetry.lock /server/

RUN pip install poetry && poetry config virtualenvs.create false && poetry install

COPY ./server /server
