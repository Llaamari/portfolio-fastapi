from fastapi.testclient import TestClient
from uuid import uuid4

from app.main import app

client = TestClient(app)


def test_create_and_list_tasks():
    email = f"user-{uuid4()}@example.com"
    password = "password123"

    # create user
    client.post("/users/", json={"email": email, "password": password})

    # login
    response = client.post(
        "/auth/login",
        data={"username": email, "password": password},
    )
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # create task
    response = client.post(
        "/tasks/",
        json={"title": "Test task"},
        headers=headers,
    )
    assert response.status_code == 200

    # list tasks
    response = client.get("/tasks/", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) == 1