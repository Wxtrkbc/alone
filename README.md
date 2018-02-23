# alone-django

### 项目介绍

[alone-django](https://github.com/Wxtrkbc/alone-django) 是自己模仿Instagram网站做的一个私人项目，属于后端部分，前端部分为[alone-vue](https://github.com/Wxtrkbc/alone-vue) ,两个项目前后端分离，两者通过REST api 接口进行联系。其中alone-django是一个基于Django的后端项目,目前基本的接口和功能都已完成，后续会继续完善相应的功能。

主要采用到知识点如下

- 整个项目完全docker化，直接使用docker-compose 来进行服务的启动和管理


- 后端项目架构为 `the web client <-> nginx <-> the socket <-> uwsgi <-> Django <-> PostgreSQL`，其中nginx 这里还用作了静态服务器，[alone-vue](https://github.com/Wxtrkbc/alone-vue) 项目的静态文件这里直接由nginx 服务器处理返回个前端
- 基于Django REST framework， 实现自动路由、序列化、 form验证、权限控制、分页、认证和URL过滤查询等
- 使用Sentry， 用来监控项目， 进行错误跟踪和分析
- 使用ELK， 用来做全文搜素和日志分析

### 使用说明

- 将[alone-django](https://github.com/Wxtrkbc/alone-django)  clone 下来，按照 docs目录下面的sentry_deploy.md首先启动sentry服务， sentry服务的docker-compose文件在dockers目录下
- 启动好sentry服务后， 登陆上去， 按照提示创建一个django项目，并且将相应的dsn记录下来，修改ins目录下面settings文件里买相应的RAVEN_CONFIG配置
- 在项目目录下面使用命令 docker-compose  up -d 启动后端服务

### 项目目录
```
├── .dockerignore
├── .gitignore
├── .gitlab-ci.yml（后续会继续结合docker完成gitlab CI 这一块）
├── README.md
├── bin（脚本文件目录）
│   └── example.sql
├── conf（配置文件目录）
│   ├── logstash.conf
│   ├── nginx.conf
│   ├── supervisord.conf
│   ├── uwsgi.ini
│   └── uwsgi_params
├── docker-compose.yml（整个项目启动文件）
├── dockers（dockerfile和一些其他服务启动文件）
│   ├── Dockerfile-nginx
│   ├── Dockerfile-web
│   ├── Dockerfile.back
│   ├── run.sh
│   └── sentry-docker-compose.yml
├── docs（文档目录）
│   ├── gitlab.md
│   └── sentry_deploy.md
├── env（环境变量目录）
│   └── web.env
├── ins（django项目入口）
│   ├── __init__.py
│   ├── app（数据模型、序列化、filter、全文搜索文档定义等目录，）
│   ├── router.py（Django REST framework 自动路由嵌套路由定义处）
│   ├── settings.py
│   ├── social（项目的业务一块的viewset目录）
│   ├── urls.py
│   ├── user（项目用户一块viewset目录）
│   ├── utils（常用的函数工具目录）
│   ├── wsgi.py
├── manage.py
├── requirements（依赖文件目录）
│   ├── base.txt
│   ├── prod.txt
│   └── test.txt		
```

### 后端效果图

- 整个项目启动的docker services

  ![docker_services](https://github.com/Wxtrkbc/alone-django/blob/master/ins/static/screenshorts/docker_services.png)

- sentry 服务的Dashboard

  ![sentry](https://github.com/Wxtrkbc/alone-django/blob/master/ins/static/screenshorts/sentry.png)

- ELK 

  ![kibana](https://github.com/Wxtrkbc/alone-django/blob/master/ins/static/screenshorts/kibana.png)

  ![elasticsearch](https://github.com/Wxtrkbc/alone-django/blob/master/ins/static/screenshorts/elasticsearch.png)