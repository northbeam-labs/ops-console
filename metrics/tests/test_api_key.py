from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_list_api_keys():
    assert client.get("/api_keys").status_code in (200, 422)
