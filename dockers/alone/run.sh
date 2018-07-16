#!/usr/bin/env bash

#cd "$(dirname "$0")"
python3 manage.py makemigrations app
python3 manage.py makemigrations
python3 manage.py migrate app
python3 manage.py migrate
#echo y | python3 manage.py search_index --rebuild
#/usr/bin/supervisord --nodaemon
/usr/local/bin/uwsgi  --ini /alone/dockers/alone/uwsgi.ini
