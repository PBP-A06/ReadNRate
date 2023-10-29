from django.urls import path
from user_profile.views import *

urlpatterns = [
    path("show-books", show_books, name="show_books")
]