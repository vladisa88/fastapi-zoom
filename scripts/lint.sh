#!/usr/bin/env bash

pylint --verbose app tests --ignore=alembic
black app tests --check --line-length 79
flake8 app tests --exclude app/alembic,__init__.py
