from rest_framework import generics
from django_filters import rest_framework as filters
from ...models import Post

class PostFilter(filters.FilterSet):
    """Filter for Post model"""
    class Meta:
        model = Post
        fields = {
            'title': ['exact', 'in'],
            'author': ['exact'],
            'status': ['exact'],
        }
        
        