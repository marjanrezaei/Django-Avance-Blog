from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from datetime import datetime
from accounts.models import User


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user(db):
    user = User.objects.create_user(
        email='testuser@example.com',
        password='testpassword', is_verified=True
    )
    return user

@pytest.mark.django_db
class TestPostApi:

    def test_get_post_response_200(self, api_client):
        url = reverse("blog:api-v1:post-list")
        response = api_client.get(url)
        assert response.status_code == 401

    def test_create_post_response_201_status(self, api_client, create_user):
        # login the user
        api_client.force_login(user=create_user)
        # Authenticate the user
        api_client.force_authenticate(user=create_user)        
        # Create a post
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "Test Post",
            "content": "This is a test post.",
            "status": True,
            "published_at": datetime.now(),
        }
        response = api_client.post(url, data)
        assert response.status_code == 201
