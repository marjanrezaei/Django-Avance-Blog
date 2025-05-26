from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models import User, Profile
from blog.models import Post, Category
import random
from datetime import datetime

category_list = [
    "Technology",
    "Health",
    "Travel",
    "Food",
    "Lifestyle",
    "Education",
    "Finance",
    "Entertainment",
    "Sports",
    "Fashion"
]

class Command(BaseCommand):
    help = "Inserting dummy data"
    
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(
            email=self.fake.email(),
            password="@@mar1111",
      
        )
        profile = Profile.objects.get(user=user)
        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.description = self.fake.paragraph(nb_sentences=3)
        profile.save()
    
        for category_name in category_list:
            Category.objects.get_or_create(name=category_name)
            
        for _ in range(10):
            Post.objects.create(
                author=profile,
                title=self.fake.sentence(nb_words=6),
                content=self.fake.paragraph(nb_sentences=5),
                status=random.choice([True, False]),
                category=Category.objects.get(name=random.choice(category_list)),
                published_at=datetime.now(),
            )
         
    
          