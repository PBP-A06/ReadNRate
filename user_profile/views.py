from django.shortcuts import render
from book.models import Book
from bookReview.models import Review
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user_profile.models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def show_profile(request):
    books_read = Book.objects.filter(review__user=request.user).distinct()
    bookmarked_books = Book.objects.filter(bookmarked_by=request.user)
    liked_books = Book.objects.filter(liked_by=request.user)

    context = {
        'books_read': books_read,
        'bookmarked_books': bookmarked_books,
        'liked_books': liked_books,
    }
    return render(request, "profile.html", context)

@login_required(login_url='/login')
def show_profile_json(request):
    books_read = Book.objects.filter(review__user=request.user).distinct()
    bookmarked_books = Book.objects.filter(bookmarked_by=request.user)
    liked_books = Book.objects.filter(liked_by=request.user)

    # Serialize the data into JSON format
    serialized_data = {
        'books_read': list(books_read.values()),  # Serialize queryset to a list of dictionaries
        'bookmarked_books': list(bookmarked_books.values()),
        'liked_books': list(liked_books.values()),
    }

    return JsonResponse(serialized_data, safe=False)  # Return serialized data as JSON response