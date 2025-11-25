import requests
from src.config.settings import BASE_URL, REQUEST_TIMEOUT


class UsersClient:
    def __init__(self, base_url: str | None = None):
        self.base_url = base_url or BASE_URL
        self.session = requests.Session()
        self.timeout = REQUEST_TIMEOUT

    def get_users(self, page: int = 1):
        url = f"{self.base_url}/api/users"
        params = {"page": page}
        return self.session.get(url, params=params, timeout=self.timeout)

    def create_user(self, payload: dict):
        url = f"{self.base_url}/api/users"
        return self.session.post(url, json=payload, timeout=self.timeout)

    def update_user(self, user_id: int, payload: dict):
        url = f"{self.base_url}/api/users/{user_id}"
        return self.session.put(url, json=payload, timeout=self.timeout)

    def delete_user(self, user_id: int):
        url = f"{self.base_url}/api/users/{user_id}"
        return self.session.delete(url, timeout=self.timeout)
