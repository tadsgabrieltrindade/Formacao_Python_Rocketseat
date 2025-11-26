import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'

def test_status():
    response = requests.get(f"{BASE_URL}")
    response_json = response.json()
    
    assert response.status_code == 200
    assert response_json["message"] == "API running"


def test_login():
    req_body = {
        "username": "admin",
        "password": "123"
    }

    response = requests.post(f"{BASE_URL}/login", json=req_body)
    response_json = response.json()

    assert response.status_code == 200
    assert response_json["message"] == "Usuário autenticado com sucesso!"

