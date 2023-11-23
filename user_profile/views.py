from django.shortcuts import render
from book.models import Book
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user_profile.models import *
from django.contrib.auth.decorators import login_required

@csrf_exempt
def get_books(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def show_bookmarked(request):
    books = Book.objects.filter(bookmarkedbook=True)
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


@login_required(login_url='/login')
def show_profile(request):
    bookmarked_books = BookmarkedBook.objects.filter(user=request.user)
    liked_books = LikedBook.objects.filter(user=request.user)

    context = {
        'bookmarked_books': bookmarked_books,
        'liked_books': liked_books,
    }
    return render(request, "profile.html", context)

    # return JsonResponse(context)  # Return the context as JSON
