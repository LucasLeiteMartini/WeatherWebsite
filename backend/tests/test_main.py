"""TODO add comentários"""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    """TODO add comentários"""

    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
