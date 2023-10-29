from django.urls import path, include
from books.views import *

app_name = 'books'

urlpatterns = [
    path('', show_books, name = 'show_books'),
]