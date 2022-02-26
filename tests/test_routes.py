from fastapi.testclient import TestClient

from api import app

client = TestClient(app)

def test_main():
    response = client.get('/api/users/')
    assert response.status_code == 200

    response = client.get('/api/users/1')
    assert response.status_code == 200