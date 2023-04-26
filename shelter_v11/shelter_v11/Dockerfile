# pull official base image
FROM python:3.9

RUN apt update -y && apt upgrade -y

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV HOME=/home/app
ENV APP_HOME=/home/app/web

# set work directory
WORKDIR $APP_HOME

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY .. .