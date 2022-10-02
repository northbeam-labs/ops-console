from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_list_users():
    assert client.get("/users").status_code in (200, 422)
