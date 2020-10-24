#!/bin/sh

docker image build --no-cache --pull -t docky-api .
docker container stop docky-api && docker container rm docky-api
docker container run --name docky-api -p 8081:8081 -d docky-api
