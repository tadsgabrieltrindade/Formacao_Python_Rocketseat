import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'

session = requests.Session()

def test_status():
    response = requests.get(f"{BASE_URL}")
    response_json = response.json()
    
    assert response.status_code == 200
    assert response_json["message"] == "API running"



def test_create_user_sucess():
     req_body = {
        "username": "user_teste",
        "password": "123"
    }
     
     response = requests.post(f"{BASE_URL}/user", json=req_body)
     response_json = response.json()
     
     assert response.status_code == 201
     assert response_json["message"] == "Usuário cadastrado com sucesso!"


def test_create_user_invalid():
     req_body = {
        "username": "user_teste"
    }
     
     response = session.post(f"{BASE_URL}/user", json=req_body)
     response_json = response.json()
     
     assert response.status_code == 401
     assert response_json["message"] == "Dados inválidos!"



def test_login():
    req_body = {
        "username": "user_teste",
        "password": "123"
    }

    response = session.post(f"{BASE_URL}/login", json=req_body)
    response_json = response.json()

    assert response.status_code == 200
    assert response_json["message"] == "Usuário autenticado com sucesso!"

def test_logout():
    response = session.post(f"{BASE_URL}/logout")
    
    assert response.status_code == 200



def test_logout_without_session():
    response = session.post(f"{BASE_URL}/logout")
    
    assert response.status_code == 405

def test_get_user():
     #fazer o login
     req_body_login = {
        "username": "user_teste",
        "password": "123"
    }
     session.post(f"{BASE_URL}/login", json=req_body_login)
     
     response = session.get(f"{BASE_URL}/user/1")
     response_json = response.json()

     assert response.status_code == 200
     assert "username" in response_json

     

def test_update_senha():
     #fazer o login
     req_body_login = {
        "username": "user_teste",
        "password": "123"
    }
     session.post(f"{BASE_URL}/login", json=req_body_login)
    
     req_body_update = {
        "password": "1234"
    }
     response = session.put(f"{BASE_URL}/user/1", json=req_body_update)

     assert response.status_code == 200
     
     response_json = response.json()

     assert response_json["message"] == "Senha do usuário atualizada com sucesso!"




def test_delete_user():
    #fazer o login
     req_body_login = {
        "username": "user_teste",
        "password": "1234"
    }
     response = session.post(f"{BASE_URL}/login", json=req_body_login)
     

    #deletar o login
     req_body = {
        "username": "user_teste"
    }
     response = session.delete(f"{BASE_URL}/user", json=req_body)
     response_json = response.json()
     
     assert response.status_code == 200
     assert response_json["message"] == "Usuário removido com sucesso!"

     



