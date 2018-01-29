FROM nginx:latest
MAINTAINER 'Wang Dong' melodywangdong@gmail.com

COPY ./conf/nginx.conf /etc/nginx/nginx.conf
COPY ./conf/nginx.conf /etc/nginx/sites-available/

RUN mkdir -p /etc/nginx/sites-enabled/\
    && ln -s /etc/nginx/nginx.conf /etc/nginx/sites-enabled/nginx.conf

CMD ["nginx", "-g", "daemon off;"]