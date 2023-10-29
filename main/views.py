from django.shortcuts import render
from book.models import Book
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def show_main(request):
    books = Book.objects.all()
    context = {
        'books':books,
    }
    return render(request, "main.html", context)

@csrf_exempt
def show_books(request):
    books = Book.objects.all()
    context = {
        'books':books,
    }
    return render(request, "books.html", context)

@csrf_exempt
def get_books(request):
    books = Book.objects.all()
    return HttpResponse(serializers.serialize("json", books), content_type="application/json")