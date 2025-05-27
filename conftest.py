import pytest
from rest_framework.test import APIClient
from users.models import CustomUser


@pytest.fixture
def user():
    return CustomUser.objects.create_user(
        email="test@example.com", password="password"
    )


@pytest.fixture
def auth_client(user):
    client = APIClient()
    resp = client.post(
        "/auth/login/",
        {"email": user.email, "password": "password"},
        format="json",
    )
    token = resp.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return client
