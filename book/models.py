from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.TextField(null=True, blank=True)
    category = models.TextField(null=True, blank=True)
    number_of_reviews = models.IntegerField(null=True, blank=True)
    book_description = models.TextField(null=True, blank=True)
    image_link = models.TextField(null=True, blank=True)
    stars = models.IntegerField(null=True, blank=True)
    likes = models.IntegerField(default=0)
    liked_by = models.ManyToManyField(User, related_name='liked_books', blank=True)

    def __str__(self):
        return self.title
    
