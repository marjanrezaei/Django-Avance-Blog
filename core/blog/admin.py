from django.contrib import admin
from .models import Category, Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = [
        "author",
        "title",
        "status",
        "category",
        "created_at",
        "published_at",
    ]


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
