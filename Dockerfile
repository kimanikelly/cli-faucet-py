# syntax=docker/dockerfile:1

FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -i https://test.pypi.org/simple/ smart-contracts-sdk==1.0.3

RUN pip3 install -r requirements.txt

COPY . .

