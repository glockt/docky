FROM python:latest

ENV HOME=/api/data
WORKDIR $HOME
COPY api.py .

RUN apt-get -y update
RUN pip3 install Flask waitress gunicorn

EXPOSE 8081

