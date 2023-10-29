from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
<<<<<<< HEAD
    title = models.TextField(null=True, blank=True)
    category = models.TextField(null=True, blank=True)
    number_of_reviews = models.IntegerField(null=True, blank=True)
    book_description = models.TextField(null=True, blank=True)
    image_link = models.TextField(null=True, blank=True)
    stars = models.IntegerField(null=True, blank=True)
    likes = models.IntegerField(default=0)
=======
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField(null=True, blank=True)
    genre = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
>>>>>>> f13d8d2601e32e2470cd9060b6290cfca1c6ebe1

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=255)
<<<<<<< HEAD
    name = models.CharField(max_length=255)
=======
    profile_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    
>>>>>>> f13d8d2601e32e2470cd9060b6290cfca1c6ebe1
