from fastapi.testclient import TestClient
from uuid import uuid4

from app.main import app

client = TestClient(app)


def test_create_user():
    email = f"user-{uuid4()}@example.com"

    response = client.post(
        "/users/",
        json={"email": email, "password": "password123"},
    )

    assert response.status_code == 201
    data = response.json()
    assert data["email"] == email
    assert data["is_active"] is True
