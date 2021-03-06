FROM python:3.8-alpine
MAINTAINER Alex Woolford

ENV PYTHONUNBUFFERED 1

RUN apk add --update-cache \
    gcc \
    libc-dev \
    mariadb-connector-c-dev

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
