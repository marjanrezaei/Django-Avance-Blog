from django.test import TestCase
from datetime import datetime

from ..models import Post
from accounts.models import User, Profile


class TestPostModel(TestCase):
    
    def test_create_post_with_valid_data(self):
        user = User.objects.create_user(email="testuser@example.com", password="@@marjan123")
        profile = Profile.objects.create(
            user=user,
            first_name="Test",
            last_name="User",
            description="This is a test user.",
        )
        post = Post.objects.create(
            author=profile,
            title="Test Post",
            content="This is a test post.",
            status=True,
            category=None,
            published_at=datetime.now(),
        )
        self.assertEqual(post.title, "Test Post")
     