FROM ubuntu:latest
MAINTAINER 'Wang Dong' melodywangdong@gmail.com

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    python3 \
    python3-dev \
    python3-pip \
    supervisor \
    nginx \
    sqlite3 && \
	pip3 install -U pip setuptools &&  rm -rf /var/lib/apt/lists/*

RUN pip3 install supervisor-stdout
RUN pip3 install uwsgi

RUN rm -rf /etc/nginx/sites-enabled/default
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

RUN mkdir -p /var/log/alone/ && chmod 755 /var/log/alone/
RUN mkdir -p /var/log/uwsgi/

COPY . /alone
WORKDIR /alone

RUN pip3 install -r requirements.txt


RUN ln -s /alone/conf/nginx.conf /etc/nginx/sites-enabled/nginx.conf
RUN ln -s /alone/conf/supervisord.conf /etc/supervisord.conf

RUN chmod a+x /alone/run.sh
