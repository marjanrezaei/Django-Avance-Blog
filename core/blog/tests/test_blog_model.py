from django.test import TestCase
from datetime import datetime

from ..models import Post
from accounts.models import User, Profile


class TestPostModel(TestCase):
    
    def setUp(self):
        # Create a user and profile for testing
        self.user = User.objects.create_user(email="testuser@example.com", password="@@marjan123")
        self.profile = Profile.objects.create(
        user=self.user,
        first_name="Test",
        last_name="User",
        description="This is a test user.",
        )
    
    def test_create_post_with_valid_data(self):
        post = Post.objects.create(
            author=self.profile,
            title="Test Post",
            content="This is a test post.",
            status=True,
            category=None,
            published_at=datetime.now(),
        )
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
        # self.assertEqual(post.title, "Test Post")
     