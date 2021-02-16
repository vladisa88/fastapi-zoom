#!/usr/bin/env bash

alembic upgrade head
uvicorn main:app --reload --port=$BACK_END_PORT --host=0.0.0.0

exec "$@"