from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_list_organizations():
    assert client.get("/organizations").status_code in (200, 422)
