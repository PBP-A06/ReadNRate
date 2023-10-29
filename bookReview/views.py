from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from book.models import Book
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# @login_required
# def book_detail(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     context = {
#         'book': book,
#     }
#     return render(request, "book_detail.html", context)


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

    has_liked = request.user in book.liked_by.all()
    context = {'book': book, 'reviews': reviews, 'form': form, 'bookId': id, 'has_liked': has_liked, 'total_likes': book.liked_by.count()}
    return render(request, 'book_detail.html', context)

@csrf_exempt
def add_review_ajax(request, id):
    if request.method == 'POST':
        review_text = request.POST.get("review_text")

        review = Review.objects.create(
            user=request.user,
            book=Book.objects.get(id=id),
            review_text=review_text,
        )

        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()

def submit_review(request):
    if request.method == 'POST' and request.is_ajax():
        review_text = request.POST.get('review_text')
        book_id = request.POST.get('book_id')
        review = Review(text=review_text, book_id=book_id)
        review.save()

        return JsonResponse({'success': True, 'review_text': review_text})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})

def toggle_bookmark(request):
    if request.method == "POST":
        book_id = request.POST.get('book_id')
        # user = request.user
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

@csrf_exempt
def toggle_like(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.user in book.liked_by.all():
        book.liked_by.remove(request.user)
    else:
        book.liked_by.add(request.user)
    
    total_likes = book.liked_by.count()  # Menghitung jumlah like yang diperbarui
    return JsonResponse({'status': 'success', 'total_likes': total_likes})