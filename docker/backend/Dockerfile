# pull official base image
FROM python:3.9.0-alpine

ENV HOME /usr/src/backend
# set work directory
WORKDIR $HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1 \
	TZ=Europe/Kyiv \
	LANG=C.UTF-8

# install dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev openssl libffi-dev openssl-dev \
	&& pip install --upgrade pip

COPY ./backend/src/requirements  ./requirements

RUN pip install -r ./requirements/local.txt
# copy entrypoint.sh
COPY ./docker/backend/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# copy project
COPY ./backend /usr/src/backend/
