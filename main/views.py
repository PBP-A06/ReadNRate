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