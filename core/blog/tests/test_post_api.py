from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from datetime import datetime


@pytest.mark.django_db
class TestPostApi:
    client = APIClient()
    
    def test_get_post_response_200(self, django_user_model):
        url = reverse("blog:api-v1:post-list")
        response = self.client.get(url)
        assert response.status_code == 401
     
    def test_create_post_response_401_status(self):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "Test Post",
            "content": "This is a test post.",
            "status": True,
            "published_at": datetime.now(),
        }
        response = self.client.post(url, data)
        assert response.status_code == 401
