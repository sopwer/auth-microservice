from unittest import TestCase
from fastapi.testclient import TestClient
from apps import app
from database import client_db

client = TestClient(app)


class LoginTest(TestCase):

    def setUp(self) -> None:
        payload = {
            "email": "ramdani@sopwer.net",
            "fullname": "ramdani",
            "password": "r@mdni2018",
            "password2": "r@mdni2018"
        }
        response = client.post("/auth/register", json=payload)

    def test_valid_login(self):
        payload = {
            "username": "ramdani@sopwer.net",
            "password": "r@mdni2018"
        }
        response = client.post("/auth/jwt/login", data=payload)
        assert response.status_code == 200
        assert response.json()['token_type'] == 'bearer'
        assert len(response.json()['access_token']) > 1

    def test_invalid_login(self):
        payload = {
            "username": "ramdani@sopwer.net",
            "password": "salahpassword"
        }
        response = client.post("/auth/jwt/login", data=payload)
        assert response.status_code == 400 or 401
        assert response.json()['detail'] == 'LOGIN_BAD_CREDENTIALS'

    def tearDown(self) -> None:
        client_db.drop_database('test')
