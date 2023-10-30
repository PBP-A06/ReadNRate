from django.shortcuts import render
<<<<<<< HEAD
=======
from django.core import serializers
from django.http import HttpResponse
>>>>>>> 6a1c430d01e2a239e09ffe14e7815a9c2d29f0be
from django.views.decorators.csrf import csrf_exempt
from book.models import Book
from leaderboard.views import *

@csrf_exempt
<<<<<<< HEAD
=======
def get_books(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
>>>>>>> 6a1c430d01e2a239e09ffe14e7815a9c2d29f0be
def show_books(request):
    books = Book.objects.all()
    context = {
        'books':books,
    }
    return render(request, "books.html", context)