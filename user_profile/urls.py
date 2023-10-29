from django.urls import path
from user_profile.views import *

urlpatterns = [
    # path('', ),
    path("show-bookmarked/", show_bookmarked, name="show_bookmarked"),
    path("show-liked/", show_liked, name="show_liked"),
    path("", show_profile, name="show_profile")
]