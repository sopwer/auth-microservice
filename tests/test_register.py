from unittest import TestCase
from fastapi.testclient import TestClient
from apps import app
from database import client_db

# app.dependency_overrides[get_db]

client = TestClient(app)


class RegisterTest(TestCase):

    def setUp(self) -> None:
        pass

    def test_valid_register(self):
        payload = {
            "email": "ramdani@sopwer.net",
            "fullname": "ramdani",
            "password": "r@mdni2018",
            "password2": "r@mdni2018"
        }
        response = client.post("/auth/register", json=payload)
        assert response.status_code == 201

    def test_invalid_register(self):
        payload = {
            "email": "ramdani@sopwer.net",
            "fullname": "ramdani",
            "password": "r@mdni2018",
            "password2": "r@mdni2018"
        }
        client.post("/auth/register", json=payload)

        #test duplicate email
        response = client.post("/auth/register", json=payload)

        assert response.status_code == 400
        assert response.json()['detail'] == 'REGISTER_USER_ALREADY_EXISTS'

        #test unmatched password
        payload = {
            "email": "ramdani@sopwer.net",
            "fullname": "ramdani",
            "password": "r@mdniqweqweq",
            "password2": "r@mdni2018"
        }
        response = client.post("/auth/register", json=payload)

        assert response.status_code == 422
        # assert response.json()['detail'] == 'REGISTER_USER_ALREADY_EXISTS'

    def tearDown(self) -> None:
        client_db.drop_database('test')
