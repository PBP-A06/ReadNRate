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
    books_read = Review.objects.filter(user=request.user)
    bookmarked_books = Book.objects.filter(bookmarked_by=request.user)
    liked_books = Book.objects.filter(liked_by=request.user)

    context = {
        'books_read': books_read,
        'bookmarked_books': bookmarked_books,
        'liked_books': liked_books,
    }
    return render(request, "profile.html", context)
