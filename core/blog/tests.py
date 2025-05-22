from django.test import TestCase
from django.urls import reverse, resolve
from .views import IndexView

# Create your tests here. 
class TestUrl(TestCase):
    
    def test_blog_index_url_resolves(self):
        url = reverse('blog:index')
        self.assertEqual(resolve(url).func.view_class, IndexView)
 
