from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User, Profile
from ..models import Post, Category
from datetime import datetime

class TestBlogView(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email="testuser@example.com", password="@@marjan123")
        self.profile = Profile.objects.create(
        user=self.user,
        first_name="Test",
        last_name="User",
        description="This is a test user.",
        )
        self.post = Post.objects.create(
            author=self.profile,
            title="Test Post",
            content="This is a test post.",
            status=True,
            category=None,
            published_at=datetime.now(),
        )
        
    def test_blog_index_url_successful_response(self):
        url = reverse("blog:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(str(response.content).find("index"))
        self.assertTemplateUsed(response, template_name="index.html")
        
    def test_blog_post_detail_lagged_in_response(self):
       pass
   
   # for user not logged in
    def test_blog_post_detail_anonymous_response(self):
        url = reverse("blog:post-detail", kwargs={"pk": self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)