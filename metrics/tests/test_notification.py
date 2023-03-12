from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_list_notifications():
    assert client.get("/notifications").status_code in (200, 422)
