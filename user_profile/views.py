from django.shortcuts import render
from user_profile.models import Book
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def get_books(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def show_bookmarked(request):
    books = Book.objects.filter(bookmarked=True)
    context = {
        'books':books,
    }
    return render(request, "profile.html", context)

@csrf_exempt
def show_liked(request):
    books = Book.objects.filter(liked=True)
    context = {
        'books':books,
    }
    return render(request, "profile.html", context)