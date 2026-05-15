import pytest
from fastapi.testclient import TestClient
from main import app, db

client = TestClient(app)

@pytest.fixture(autouse=True)
def clean(): db.clear()

def test_get_all(): assert client.get("/patients").status_code == 200
def test_create():
    p = {"id": 1, "full_name": "Alex", "oms_policy": "1234567890123456", "birth_date": "2000-01-01", "email": "a@b.com", "gender": "Male"}
    assert client.post("/patients", json=p).status_code == 201
def test_404(): assert client.get("/patients/99").status_code == 404
def test_dup():
    p = {"id": 1, "full_name": "Alex", "oms_policy": "1234567890123456", "birth_date": "2000-01-01", "email": "a@b.com", "gender": "Male"}
    client.post("/patients", json=p)
    assert client.post("/patients", json=p).status_code == 400
def test_put():
    p = {"id": 1, "full_name": "Alex", "oms_policy": "1234567890123456", "birth_date": "2000-01-01", "email": "a@b.com", "gender": "Male"}
    client.post("/patients", json=p)
    p["full_name"] = "New"
    assert client.put("/patients/1", json=p).status_code == 200
def test_del():
    p = {"id": 1, "full_name": "Alex", "oms_policy": "1234567890123456", "birth_date": "2000-01-01", "email": "a@b.com", "gender": "Male"}
    client.post("/patients", json=p)
    assert client.delete("/patients/1").status_code == 204
def test_bad_oms():
    p = {"id": 1, "full_name": "Alex", "oms_policy": "123", "birth_date": "2000-01-01", "email": "a@b.com", "gender": "Male"}
    assert client.post("/patients", json=p).status_code == 422
def test_bad_gender():
    p = {"id": 1, "full_name": "Alex", "oms_policy": "1234567890123456", "birth_date": "2000-01-01", "email": "a@b.com", "gender": "Other"}
    assert client.post("/patients", json=p).status_code == 422