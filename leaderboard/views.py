from django.shortcuts import render
from book.models import Book
# from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
# from django.urls import reverse
# from django.core import serializers
# from django.shortcuts import redirect
# from leaderboard.forms import 

def leaderboad_option(request):
    books = Book.objects.all()
    context = {
        'books':books,
    }
    return render(request, "leaderboard.html", context)