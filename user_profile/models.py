from django.db import models
<<<<<<< HEAD
import book.models
=======
>>>>>>> 6a1c430d01e2a239e09ffe14e7815a9c2d29f0be
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
<<<<<<< HEAD
    book = models.OneToOneField(book.models.Book, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # title = models.TextField(null=True, blank=True)
    # category = models.TextField(null=True, blank=True)
    # number_of_reviews = models.IntegerField(null=True, blank=True)
    # book_description = models.TextField(null=True, blank=True)
    # image_link = models.TextField(null=True, blank=True)
    # stars = models.IntegerField(null=True, blank=True)
    # likes = models.IntegerField(default=0)
    bookmarked = models.BooleanField(default=False)
    liked = models.BooleanField(default=False)
=======
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField(null=True, blank=True)
    genre = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
>>>>>>> 6a1c430d01e2a239e09ffe14e7815a9c2d29f0be

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=255)
<<<<<<< HEAD
    name = models.CharField(max_length=255)
=======
    profile_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    
>>>>>>> 6a1c430d01e2a239e09ffe14e7815a9c2d29f0be
