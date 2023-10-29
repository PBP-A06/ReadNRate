from django.urls import path
from book.views import *
app_name = "book"

urlpatterns = [
    path("", show_books, name="show_books"),
    path("api/", get_books, name="get_books"),
]