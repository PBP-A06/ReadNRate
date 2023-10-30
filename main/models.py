from django.db import models
from book.models import Book

class User(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

class Readlist(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    books = models.ManyToManyField(Book, blank=True, related_name='main_books')
 
    def __str__(self):
        return self.title
