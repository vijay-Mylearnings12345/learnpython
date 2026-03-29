"""
Simple API testing examples using the `requests` library.

Before running these examples, install requests:
    pip install requests

The module demonstrates basic GET and POST operations against
httpbin.org, which provides a simple HTTP request & response service.
"""

import requests


def test_get():
    """Perform a basic GET request."""
    url = "https://httpbin.org/get"
    params = {"sample": "value"}
    response = requests.get(url, params=params)
    print("GET status:", response.status_code)
    print("GET response JSON:", response.json())


def test_post():
    """Perform a basic POST request with JSON data."""
    url = "https://httpbin.org/post"
    payload = {"name": "Alice", "age": 30}
    response = requests.post(url, json=payload)
    print("POST status:", response.status_code)
    print("POST response JSON:", response.json())


if __name__ == "__main__":
    print("---- Running API tests ----")
    test_get()
    print()
    test_post()
