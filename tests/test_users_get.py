from http import HTTPStatus
from src.models.user_models import User


def test_get_users_returns_200(users_client):
    response = users_client.get_users(page=1)

    assert response.status_code == HTTPStatus.OK

    body = response.json()
    assert "data" in body
    assert isinstance(body["data"], list)
    assert len(body["data"]) > 0

    # Validate first user using pydantic model
    user = User(**body["data"][0])
    assert "@" in user.email
