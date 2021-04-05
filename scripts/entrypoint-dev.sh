#!/usr/bin/env bash

uvicorn main:app --reload --port=$BACK_END_PORT --host=0.0.0.0

exec "$@"
