# docky
A small project to explore docker, docker-compose and kubernetes.

## Images
Under `images/` are different docker images with for differen functionality.
* `images/api`: The api image is a python image running flask. It contains a Dockerfile and a helper script to get it up and running. The api takes a parameter  ̀name ̀, but can be omitted. The answer is json encoded.
*  `images/web`: The web image is a nginx image running nginx. . It acts as a frontend for the api.

## docker-compose
Under `docker-compose/` is a docker-compose file as well as a short script which starts it.