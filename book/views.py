from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from book.models import Book
from leaderboard.views import *

@csrf_exempt
def get_books(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def show_books(request):
    books = Book.objects.all()
    context = {
        'books':books,
    }
    return render(request, "books.html", context)