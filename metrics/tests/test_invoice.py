from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_list_invoices():
    assert client.get("/invoices").status_code in (200, 422)
