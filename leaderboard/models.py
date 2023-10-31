from django.db import models
from book.models import Book
from readlist.models import Readlist

class RatingLeaderboardEntry(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
