"""Small REST API client used by the example workflow."""

from typing import Any

import requests


class MockAPIClient:
    """A tiny JSON REST client for fetching input text and posting results."""

    def __init__(self, base_url: str, timeout: float = 10.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def fetch_data(self) -> str:
        """Fetch text from ``GET /data``.

        Raises:
            ValueError: If the response JSON does not contain a string ``text`` field.
            requests.HTTPError: If the server returns an unsuccessful status code.
        """
        response = requests.get(f"{self.base_url}/data", timeout=self.timeout)
        response.raise_for_status()
        text = response.json().get("text", "")
        if not isinstance(text, str):
            raise ValueError("API response field 'text' must be a string")
        return text

    def post_result(self, result: str) -> dict[str, Any]:
        """Post transformed text to ``POST /result`` and return the JSON response."""
        response = requests.post(
            f"{self.base_url}/result",
            json={"result": result},
            timeout=self.timeout,
        )
        response.raise_for_status()
        payload = response.json()
        if not isinstance(payload, dict):
            raise ValueError("API response must be a JSON object")
        return payload
