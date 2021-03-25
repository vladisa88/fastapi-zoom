# pylint:disable=(missing-function-docstring, redefined-outer-name)
# pylint:disable=(unused-import)
import random
import typing as tp

import pytest

from services.functions import get_accounts


@pytest.fixture()
def request_body() -> dict[str, str]:
    accounts = get_accounts()
    return {"email": random.choice(accounts)}


def test_populate_accounts(client: tp.Generator) -> None:
    with client as api_client:
        response = api_client.post("/populate")
    assert response.status_code == 200


def test_fetch_accounts(client: tp.Generator) -> None:
    with client as api_client:
        response = api_client.get("/accounts")
    objects = response.json()
    assert len(objects) == 5


def test_fetch_one_account(client: tp.Generator) -> None:
    with client as api_client:
        response = api_client.get("/accounts/1")
    object_ = response.json()
    keys = object_.keys()
    assert "email" in keys
    assert object_["id"] == 1


def test_patch_account(
    client: tp.Generator, request_body: dict[str, str]
) -> None:
    with client as api_client:
        response = api_client.patch("/accounts/", json=request_body)
    object_ = response.json()
    assert object_["is_using"] is False
