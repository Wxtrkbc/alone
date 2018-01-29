FROM ubuntu:latest
MAINTAINER 'Wang Dong' melodywangdong@gmail.com

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    python3 \
    python3-dev \
    python3-pip && \
	pip3 install -U pip setuptools &&  rm -rf /var/lib/apt/lists/*

RUN pip3 install uwsgi


RUN mkdir -p /var/log/alone/ && chmod 755 /var/log/alone/
RUN mkdir -p /var/log/uwsgi/

COPY . /alone
WORKDIR /alone

RUN pip3 install -r requirements.txt
RUN chmod a+x ./dockers/run.sh
