FROM python:3.6

LABEL maintainer="hello@horbit7.ch"
LABEL description="talentlab web page"

ENV LANG C.UTF-8
ENV WORKDIR /root/code/
ENV PYTHONPATH server
ENV PYTHONUNBUFFERED 1
ENV SHELL bash

RUN mkdir ${WORKDIR}
RUN apt-get update && apt-get install -yq git htop vim tmux libmemcached-dev zlib1g-dev gettext

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs

RUN npm install -g sass

RUN pip3 install pipenv

ADD . ${WORKDIR}
WORKDIR ${WORKDIR}

RUN pipenv install --dev
RUN npm install --prefix client