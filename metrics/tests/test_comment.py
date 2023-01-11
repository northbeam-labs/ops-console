from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_list_comments():
    assert client.get("/comments").status_code in (200, 422)
