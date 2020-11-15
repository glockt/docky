FROM python:latest

ENV HOME=/api/data
WORKDIR $HOME
COPY *.py ./

RUN apt-get -y update
RUN pip3 install fastapi uvicorn psycopg2 config

EXPOSE 8081
