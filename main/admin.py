from django.contrib import admin
from .models import Book
from readlist.models import Readlist
from leaderboard.models import RatingLeaderboardEntry

admin.site.register(Book)
admin.site.register(Readlist)
admin.site.register(RatingLeaderboardEntry)