# pull official base image
FROM python:3.9.0-alpine

ENV HOME /usr/src/iot
# set work directory
WORKDIR $HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1 \
	TZ=Europe/Kyiv \
	LANG=C.UTF-8

# install dependencies
RUN pip install --upgrade pip

COPY ./iot/requirements.txt  .

RUN pip install -r ./requirements.txt

# copy entrypoint.sh
COPY ./docker/iot/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# copy project
COPY ./iot /usr/src/iot/
