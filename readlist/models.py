from django.db import models
from book.models import Book
from django.contrib.auth.models import User

# Create your models here.

class Readlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    books = models.ManyToManyField(Book)
    likes = models.IntegerField(default=0)
    liked_by = models.ManyToManyField(User, related_name='liked_readlists', blank=True)