# pylint:disable=(redefined-outer-name)
import typing as tp

import pytest
from starlette.testclient import TestClient

from conf.db import engine, metadata

from app import app


@pytest.fixture(autouse=True, scope="session")
def create_test_database() -> tp.Generator:
    """
    Create tables in the database
    """
    metadata.drop_all(engine)
    metadata.create_all(engine)
    yield
    metadata.drop_all(engine)


@pytest.fixture(scope="session")
def client() -> tp.Generator:
    """
    Simply returning client object
    """
    client = TestClient(app)
    yield client
