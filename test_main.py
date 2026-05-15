import pytest
from fastapi.testclient import TestClient
from main import app, db

client = TestClient(app)

@pytest.fixture(autouse=True)
def run_before():
    """Очистка базы данных перед каждым тестом."""
    db.clear()

def test_get_all_empty():
    response = client.get("/patients")
    assert response.status_code == 200
    assert response.json() == []

def test_create_patient_success():
    payload = {
        "id": 1,
        "full_name": "Иванов Иван",
        "oms_policy": "1234567890123456",
        "birth_date": "2000-01-01",
        "email": "alex@example.com",
        "gender": "Male"
    }
    response = client.post("/patients", json=payload)
    assert response.status_code == 201

def test_get_nonexistent_returns_404():
    response = client.get("/patients/999")
    assert response.status_code == 404

def test_invalid_oms_returns_422():
    payload = {
        "id": 1,
        "full_name": "Alex",
        "oms_policy": "123",
        "birth_date": "2000-01-01",
        "email": "a@b.com",
        "gender": "Male"
    }
    response = client.post("/patients", json=payload)
    assert response.status_code == 422