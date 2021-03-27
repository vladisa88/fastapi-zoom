# FASTAPI-ZOOM

[![CodeFactor](https://www.codefactor.io/repository/github/vladisa88/fastapi-zoom/badge/master)](https://www.codefactor.io/repository/github/vladisa88/fastapi-zoom/overview/master)  ![Travis-CI](https://travis-ci.com/vladisa88/fastapi-zoom.svg?branch=master)

## This project provides you a way to interact with Zoom API via REST API

### Features:
* Fast instead of FastAPI
* Use ORMAR - the best ORM for FastAPI
* Dockerized
* Fully async
* Alembic migrations
* Use aiozoom library
* Use travis ci
* Use black, pylint, flake8, autoflake
* Tests

### To use it on your device:
```git clone https://github.com/vladisa88/fastapi-zoom.git```

**Production environment**

Rename ".env.example" to ".env" and put your own data there

```docker-compose up --build```

**If you want to run tests follow this steps:**

Rename ".env.dev.example" to ".env" and put your own data there

```docker-compose -f dev.docker-compose.yml up --build```

This will run a simple container without postgres database.
Use it only for running tests.