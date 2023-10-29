from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from book.models import Book
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# def get_books_by_id(request, id):
#     data = Book.objects.filter(pk=id)
#     data_json = serializers.serialize("json", data)
#     return HttpResponse(data_json, content_type="application/json")

# @login_required
def show_book_detail(request, id):
    book = get_object_or_404(Book, pk=id)
    reviews = Review.objects.filter(book=book)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect('show_book_detail', id=book.pk)

    else:
        form = ReviewForm()

    return render(request, 'book_detail.html', {'book': book, 'reviews': reviews, 'form': form})

# @login_required
def add_review(request, id):
    book = Book.objects.get(id=id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect('book_detail', id=book.id)
    else:
        form = ReviewForm()

    return render(request, 'review/add_review.html', {'form': form, 'book': book})

