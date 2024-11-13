from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Current-ly API!"}

# def test_create_outage():
#     payload = {"location": "Tbilisi", "outage_start": "2024-11-12T12:00:00"}
#     response = client.post("/outages", json=payload)
#     assert response.status_code == 201
#     assert response.json()["location"] == "Tbilisi"
