from django.contrib import admin
from book.models import Book
from readlist.models import Readlist
from leaderboard.models import RatingLeaderboardEntry

admin.site.register(Book)
admin.site.register(Readlist)
admin.site.register(RatingLeaderboardEntry)