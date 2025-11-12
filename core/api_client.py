import requests, json, os

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        response = requests.get(f"{self.base_url}{endpoint}")
        return response

    def post(self, endpoint, payload):
        response = requests.post(f"{self.base_url}{endpoint}", json=payload)
        return response

    def put(self, endpoint, payload):
        response = requests.put(f"{self.base_url}{endpoint}", json=payload)
        return response

    def delete(self, endpoint):
        response = requests.delete(f"{self.base_url}{endpoint}")
        return response