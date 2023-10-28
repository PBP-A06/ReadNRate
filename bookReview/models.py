from django.db import models
from django.contrib.auth.models import User
from book.models import Book

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField()
    review_text = models.TextField()
    # bookmark = models.IntegerField()

    def __str__(self):
        return self.review_text