from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_list_tasks():
    assert client.get("/tasks").status_code in (200, 422)
