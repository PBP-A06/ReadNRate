from django.db import models
from book.models import Book
from django.contrib.auth.models import User

# Create your models here.

# class Book(models.Model):
#     book = models.OneToOneField(book.models.Book, on_delete=models.CASCADE, null=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     # title = models.TextField(null=True, blank=True)
#     # category = models.TextField(null=True, blank=True)
#     # number_of_reviews = models.IntegerField(null=True, blank=True)
#     # book_description = models.TextField(null=True, blank=True)
#     # image_link = models.TextField(null=True, blank=True)
#     # stars = models.IntegerField(null=True, blank=True)
#     # likes = models.IntegerField(default=0)
#     bookmarked = models.BooleanField(default=False)
#     liked = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title

class User(models.Model):
    username = models.CharField(max_length=255)
    # profile_name = models.CharField(max_length=255, null=True)
    # name = models.CharField(max_length=255, null=True)

class BookmarkedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

class LikedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
