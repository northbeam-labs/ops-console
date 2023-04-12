from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_list_audit_logs():
    assert client.get("/audit_logs").status_code in (200, 422)
