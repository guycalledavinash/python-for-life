import requests

class MockAPIClient:
    """A simple REST client for demo purposes."""

    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_data(self):
        response = requests.get(f"{self.base_url}/data")
        response.raise_for_status()
        return response.json().get("text", "")

    def post_result(self, result):
        response = requests.post(f"{self.base_url}/result", json={"result": result})
        response.raise_for_status()
        return response.json()
