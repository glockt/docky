FROM python:latest

WORKDIR /api/data
COPY api.py .

RUN apt-get -y update
RUN pip3 install Flask waitress

EXPOSE 8081

ENTRYPOINT [ "python" ]
CMD [ "api.py" ]