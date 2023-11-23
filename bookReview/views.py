from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from book.models import Book
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

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
    has_bookmarked = request.user in book.bookmarked_by.all()
    context = {'book': book, 'reviews': reviews, 'form': form, 'bookId': id, 'has_liked': has_liked, 'has_bookmarked': has_bookmarked, 'total_likes': book.liked_by.count()}
    return render(request, 'book_detail.html', context)

@login_required
@csrf_exempt
def add_review_ajax(request, id):
    if request.method == 'POST':
        review_text = request.POST.get("review_text")

        review = Review.objects.create(
            user=request.user,
            book=Book.objects.get(id=id),
            review_text=review_text,
        )

        return JsonResponse({'success': True, 'review_text': review_text, 'username': request.user.username})
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})



@login_required
@csrf_exempt
def submit_review(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        review_text = request.POST.get('review_text')
        book_id = request.POST.get('book_id')
        review = Review(review_text=review_text, book_id=book_id)
        review.save()

        return JsonResponse({'success': True, 'review_text': review_text})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})


@csrf_exempt
def toggle_bookmark(request, id):  # Tambahkan parameter 'id'
    if request.method == "POST":
        book = get_object_or_404(Book, pk=id)
        if request.user in book.bookmarked_by.all():
            book.bookmarked_by.remove(request.user)
        else:
            book.bookmarked_by.add(request.user)

        book.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

@csrf_exempt
def toggle_like(request, id):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=id)
        if request.user in book.liked_by.all():
            book.liked_by.remove(request.user)
        else:
            book.liked_by.add(request.user)

        book.likes = book.liked_by.count()
        book.save()  # Tambahkan baris ini untuk menyimpan perubahan

        total_likes = book.liked_by.count()  # Menghitung jumlah like yang diperbarui
        return JsonResponse({'status': 'success', 'total_likes': total_likes})