#!/usr/bin/env bash

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

alembic upgrade head
uvicorn main:app --reload --port=$BACK_END_PORT --host=0.0.0.0

exec "$@"
