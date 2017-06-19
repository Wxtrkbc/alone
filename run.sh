#!/usr/bin/env bash

#cd "$(dirname "$0")"
python3 manage.py makemigrations app
python3 manage.py migrate app
/usr/bin/supervisord --nodaemon
