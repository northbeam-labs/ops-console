from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_list_tags():
    assert client.get("/tags").status_code in (200, 422)
# wip: batch-jobs
