from django.urls import path, include
from books.views import *

urlpatterns = [
    path('', show_books, name = 'show_books'),
]