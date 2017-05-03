FROM ubuntu:14.04
MAINTAINER 'Wang Dong' melodywangdong@gmail.com

RUN apt-get update && apt-get install -y python-pip python-dev openssh-client \
    libpq-dev nginx libffi-dev sqlite3 libmysqld-dev

RUN mkdir -p /var/log/alone/ && chmod 755 /var/log/alone/


#RUN easy_install supervisor
#RUN easy_install supervisor-stdout
#RUN pip install uwsgi
#
#RUN rm -rf /etc/nginx/sites-enabled/default
#RUN echo "daemon off;" >> /etc/nginx/nginx.conf

WORKDIR /alone

#EXPOSE 9600

RUN pip install -U pip
COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY . /alone
#RUN ln -s /alone/conf/nginx.conf /etc/nginx/sites-enabled/nginx.conf
#RUN ln -s /alone/conf/supervisord.conf /etc/supervisord.conf
#
#RUN chmod a+x /alone/run.sh && mkdir -p /var/log/uwsgi/
#
#CMD ["/alone/run.sh"]
