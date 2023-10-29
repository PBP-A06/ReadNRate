from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField(null=True, blank=True)
    genre = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=255)
    profile_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    
