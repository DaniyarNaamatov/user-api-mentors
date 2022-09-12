FROM python:3.10

ENV PYTHONBUFFERED 1

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt