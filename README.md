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
├── .git
├── .gitignore
├── .gitlab-ci.yml
├── README.md
├── bin
│   └── example.sql
├── config
│   ├── __init__.py
│   ├── logstash.conf
│   └── settings
│       ├── __init__.py
│       ├── base.py
│       ├── local.py
│       └── production.py
├── docker-compose.yml
├── dockers
│   ├── alone
│   ├── celery
│   ├── elk
│   ├── nginx
│   └── sentry
├── docs
│   ├── gitlab.md
│   └── sentry_deploy.md
├── env
│   └── local
├── ins(Django项目)
│   ├── __init__.py
│   ├── app  （数据模型、序列化、filter、权限，）
│   ├── celery.py
│   ├── middleware.py
│   ├── router.py
│   ├── social （社交服务）
│   ├── static
│   ├── urls.py
│   ├── user （用户服务）
│   ├── utils
│   └── wsgi.py
├── local.yml
├── manage.py
├── requirements
│   ├── base.txt
│   ├── prod.txt
│   └── test.txt
└── requirements.txt

```

### 后端效果图

- 整个项目启动的docker services

  ![docker_services](https://github.com/Wxtrkbc/alone-django/blob/master/ins/static/screenshorts/docker_services.png)

- sentry 服务的Dashboard

  ![sentry](https://github.com/Wxtrkbc/alone-django/blob/master/ins/static/screenshorts/sentry.png)
