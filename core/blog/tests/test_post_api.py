from rest_framework.test import APIClient
from django.urls import reverse
import pytest


@pytest.mark.django_db
class TestPostApi:

    def test_get_post_response_200(self, django_user_model):
        user = django_user_model.objects.create_user(email="test@example.com", password="testpass")
        client = APIClient()
        client.force_authenticate(user=user)
        url = reverse("blog:api-v1:post-list")
        response = client.get(url)
        assert response.status_code == 200
     

