import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_register_and_login():
    client = APIClient()
    reg = client.post(
        "/auth/register/",
        {"email": "a@a.com", "password": "1234"},
        format="json",
    )
    assert reg.status_code == 201 or reg.status_code == 200

    login = client.post(
        "/auth/login/", {"email": "a@a.com", "password": "1234"}, format="json"
    )
    assert login.status_code == 200
    assert "access" in login.data
