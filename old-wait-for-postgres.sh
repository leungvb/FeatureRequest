#!/bin/sh
# wait-for-postgres.sh

set -e

host="$1"
cmd="$@"

until psql postgres://victor:test123@localhost:5432/features -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd
