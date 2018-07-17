#!/bin/sh

set -o errexit
set -o nounset


celery -A ins worker -l INFO
