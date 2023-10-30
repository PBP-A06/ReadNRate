from django.urls import path
from user_profile.views import *

urlpatterns = [
<<<<<<< HEAD
    # path('', ),
    path("show-bookmarked/", show_bookmarked, name="show_bookmarked"),
    path("show-liked/", show_liked, name="show_liked"),
    path("", show_profile, name="show_profile")
=======
    path("show-books", show_books, name="show_books")
>>>>>>> 6a1c430d01e2a239e09ffe14e7815a9c2d29f0be
]