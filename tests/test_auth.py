from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_login_and_me():
    # login
    response = client.post(
        "/auth/login",
        data={"username": "user@example.com", "password": "password123"},
    )
    assert response.status_code == 200
    token = response.json()["access_token"]

    # access protected route
    response = client.get(
        "/users/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200