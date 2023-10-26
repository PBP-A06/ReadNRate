from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    numberOfReviews = models.IntegerField(null=True, blank=True)
    bookDescription = models.TextField(null=True, blank=True)
    imageLink = models.CharField(max_length=255, null=True, blank=True)
    stars = models.IntegerField(null=True, blank=True)