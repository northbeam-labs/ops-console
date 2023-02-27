from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_list_payments():
    assert client.get("/payments").status_code in (200, 422)
