from django.db import models
from book.models import Book

class User(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

