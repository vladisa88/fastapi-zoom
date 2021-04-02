# pylint:disable=(missing-function-docstring, redefined-outer-name)
# pylint:disable=(unused-import, redefined-argument-from-local)
import typing as tp

import pytest
from pytest_mock import MockerFixture


@pytest.fixture()
def create_meeting_request_body() -> dict[str, str]:
    return {"title": "Test Title"}


@pytest.fixture()
def create_meeting_method_response() -> dict[str, str]:
    return {
        "id": "123",
        "start_url": "https://test.com/",
        "join_url": "https://test.com/",
    }


def test_create_meeting(
    mocker: MockerFixture,
    client: tp.Generator,
    create_meeting_request_body: dict[str, str],
    create_meeting_method_response: dict[str, str],
) -> None:
    mocked_api_call = mocker.patch(
        "services.meeting.zoom_service.zoom.create_meeting"
    )
    mocked_api_call.return_value = create_meeting_method_response

    with client as client:
        response = client.post("/meeting", json=create_meeting_request_body)

    assert response.status_code == 200

    response_json = response.json()
    assert response_json["meeting_id"] == "123"


def test_create_meeting_fail(
    client: tp.Generator, create_meeting_request_body: dict[str, str]
) -> None:
    with client as client:
        for _ in range(4):
            client.post("/meeting", json=create_meeting_request_body)
        response = client.post("/meeting", json=create_meeting_request_body)

    assert response.status_code == 409


def test_fetch_all_meetings(client: tp.Generator) -> None:
    with client as client:
        response = client.get("/meetings")

    assert response.status_code == 200

    response_json = response.json()
    assert len(response_json) == 5


def test_fetch_meeting(
    mocker: MockerFixture,
    client: tp.Generator,
    create_meeting_method_response: dict[str, str],
) -> None:
    mocked_api_call = mocker.patch(
        "routers.zoom.zoom_service.zoom.get_meeting"
    )
    mocked_api_call.return_value = create_meeting_method_response

    meeting_id = "123"

    with client as client:
        response = client.get(f"/meeting/{meeting_id}")

    assert response.status_code == 200

    response_json = response.json()
    assert response_json["start_url"] == "https://test.com/"


def test_stop_meeting(mocker: MockerFixture, client: tp.Generator) -> None:
    mocked_api_call = mocker.patch(
        "routers.zoom.zoom_service.zoom.stop_meeting"
    )
    mocked_api_call.return_value = {}

    meeting_id = "123"

    with client as client:
        response = client.delete(f"/meeting/{meeting_id}")

    assert response.status_code == 200


def test_stop_all_meetings(
    mocker: MockerFixture, client: tp.Generator
) -> None:
    mocked_api_call = mocker.patch(
        "services.meeting.zoom_service.zoom.stop_meeting"
    )
    mocked_api_call.return_value = {}

    body = {"meetings_id": ["123", "312"]}

    with client as client:
        response = client.put("/meetings", json=body)

    assert response.status_code == 200
