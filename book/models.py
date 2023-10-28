from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.TextField(null=True, blank=True)
    category = models.TextField(null=True, blank=True)
    number_of_reviews = models.IntegerField(null=True, blank=True)
    book_description = models.TextField(null=True, blank=True)
    image_link = models.TextField(null=True, blank=True)
    stars = models.IntegerField(null=True, blank=True)