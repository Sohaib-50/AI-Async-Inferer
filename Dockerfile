FROM python:3.10

ENV using_docker="true"

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

