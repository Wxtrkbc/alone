#!/bin/sh

set -o errexit
set -o nounset


rm -f './celerybeat.pid'
celery -A ins beat -l INFO