import pytest
from core.utils import retry
from core.logger import get_logger

logger = get_logger(__name__)

@retry(3)
def test_get_user(client):
    logger.info("Testing GET /users/2")
    response = client.get("/users/2")
    assert response.status_code == 200
    assert "data" in response.json()

def test_create_user(client):
    logger.info("Testing POST /users")
    payload = {"name": "Ravi", "job": "SDET"}
    response = client.post("/users", payload)
    assert response.status_code == 201
    assert response.json()["name"] == "Ravi"
