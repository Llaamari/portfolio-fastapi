from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_login_and_me():
    # Create user before logging in
    email = "user@example.com"
    password = "password123"

    client.post(
        "/users/",
        json={"email": email, "password": password},
    )

    # login
    response = client.post(
        "/auth/login",
        data={"username": email, "password": password},
    )
    assert response.status_code == 200
    token = response.json()["access_token"]

    # access to a protected route
    response = client.get(
        "/users/me",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
