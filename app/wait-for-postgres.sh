#!/bin/sh
# wait-for-postgres.sh

# sleep 10
gunicorn --bind 0.0.0.0:8000 wsgi:app