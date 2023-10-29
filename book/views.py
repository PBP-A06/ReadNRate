from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from book.models import Book
from leaderboard.views import *

@csrf_exempt
def show_books(request):
    books = Book.objects.all()
    context = {
        'books':books,
    }
    return render(request, "all-books.html", context)