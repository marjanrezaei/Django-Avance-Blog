from django.test import TestCase
from datetime import datetime

from ..models import Category
from ..forms import PostForm


class TestPostForm(TestCase):
    
    def test_post_form_with_valid_data(self):
        category_object = Category.objects.create(name="Test Category")
        form = PostForm(data={
            "title": "Test Title",
            "content": "Test Content",
            "category": category_object,
            "status": True,
            "published_at": datetime.now(),})
        self.assertTrue(form.is_valid())
            
    def test_post_form_with_no_data(self):
        form = PostForm(data={})
        self.assertFalse(form.is_valid())