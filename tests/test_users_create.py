from http import HTTPStatus

import responses

from src.config.settings import BASE_URL
from src.models.user_models import CreateUserRequest, CreateUserResponse


@responses.activate
def test_create_user_returns_201(users_client):
    # Arrange: build request payload
    payload = CreateUserRequest(name="Komron", job="QA Engineer").dict()
    url = f"{BASE_URL}/api/users"

    # Mock the external API
    mocked_response = {
        "name": payload["name"],
        "job": payload["job"],
        "id": "123",
        "createdAt": "2025-01-01T00:00:00.000Z",
    }

    responses.add(
        method=responses.POST,
        url=url,
        json=mocked_response,
        status=HTTPStatus.CREATED,
    )

    # Act: call the real client (but responses intercepts the HTTP call)
    response = users_client.create_user(payload)

    # Assert: status code is 201
    assert response.status_code == HTTPStatus.CREATED

    # Assert: response body schema + values
    body = response.json()
    created_user = CreateUserResponse(**body)

    assert created_user.name == payload["name"]
    assert created_user.job == payload["job"]
    assert created_user.id == "123"
    assert created_user.createdAt == "2025-01-01T00:00:00.000Z"
