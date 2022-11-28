from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_list_projects():
    assert client.get("/projects").status_code in (200, 422)
