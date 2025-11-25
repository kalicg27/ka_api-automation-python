from http import HTTPStatus
from src.models.user_models import CreateUserRequest, CreateUserResponse


def test_create_user_returns_201(users_client):
    payload = CreateUserRequest(name="Komron", job="QA Engineer").dict()
    response = users_client.create_user(payload)

    assert response.status_code == HTTPStatus.CREATED

    body = response.json()
    created_user = CreateUserResponse(**body)

    assert created_user.name == payload["name"]
    assert created_user.job == payload["job"]
    assert created_user.id
    assert created_user.createdAt
