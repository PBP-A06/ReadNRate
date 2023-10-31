from django.db import models
from book.models import Book
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=255)

class BookmarkedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

class LikedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
