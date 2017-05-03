#!/usr/bin/env bash

cd "$(dirname "$0")"

if [ $TEST = "True" ]
then
  python manage.py test
else
  /usr/local/bin/supervisord --nodaemon
fi
