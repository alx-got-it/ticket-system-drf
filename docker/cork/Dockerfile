# pull official base image
FROM python:3.11.5-alpine

RUN apk update && apk add python3-dev gcc libc-dev

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install gunicorn
ADD ./requirements.txt /app/
RUN pip install -r requirements.txt

ADD ./cork /app/cork
ADD ./docker /app/docker

RUN chmod +x /app/docker/cork/server-entrypoint.sh
RUN chmod +x /app/docker/cork/worker-entrypoint.sh