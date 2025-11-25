import pytest
from src.clients.users_client import UsersClient


@pytest.fixture(scope="session")
def users_client():
    return UsersClient()
