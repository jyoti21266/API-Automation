import json, pytest
from core.api_client import APIClient

@pytest.fixture(scope="session")
def config():
    with open("config/config.json") as f:
        return json.load(f)

@pytest.fixture(scope="session")
def client(config):
    return APIClient(config["base_url"])
