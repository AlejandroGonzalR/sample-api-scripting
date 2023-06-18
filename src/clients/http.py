from typing import Any

import requests
from src.config.app_environments import APIs


class HttpClient:
    def __init__(self, api: str = 'sample_api') -> None:
        self.base_url = APIs[api]['host']
        self.headers = APIs[api]['headers'] or {}

    def get(self, endpoint: str) -> Any:
        url: str = self.base_url + endpoint
        response = requests.get(url, headers=self.headers)
        return response.json()

    # ... Add more HTTP client methods as needed, for this example, only GET requests are needed
