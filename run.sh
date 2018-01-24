#!/usr/bin/env bash

#cd "$(dirname "$0")"
python3 manage.py makemigrations app
python3 manage.py makemigrations app
python3 manage.py migrate app
python3 manage.py migrate
python3 manage.py search_index --rebuild
/usr/bin/supervisord --nodaemon
