from django.shortcuts import render
from book.models import Book
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
# from leaderboard.forms import 
from django.urls import reverse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.views.decorators.csrf import csrf_exempt

def leaderboad_option(request):
    books = Book.objects.all()
    context = {
        'books':books,
    }
    return render(request, "leaderboard.html", context)

def show_by_likes(request):
    books = Book.objects.all()
    context = {
        'books':books,
    }
    return render(request, "likes.html", context)

def show_by_rating(request):
    books = Book.objects.all()
    context = {
        'books':books,
    }
    return render(request, "rating.html", context)

def show_readlist(request):
    # nanti ambil instance readlistnya
    context = {
        'test':'testing'
    }
    return render(request, "readlist.html", context)