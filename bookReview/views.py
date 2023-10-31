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

    # Menambahkan bookId ke dalam konteks
    context = {'book': book, 'reviews': reviews, 'form': form, 'bookId': id}

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

def toggle_like(request):
    if request.method == "POST":
        review_id = request.POST.get('review_id') # Ganti dari book_id ke review_id
        try:
            review = Review.objects.get(id=review_id)
            
            # Toggle likes_count (untuk contoh ini, saya hanya menaikkan jumlah likes)
            review.likes_count += 1
            review.save()
            
            return JsonResponse({'status': 'success', 'likes': review.likes_count})
        except Review.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Review not found.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


# def get_book_json(request, book_id):
#     book = Book.objects.get(id=book_id)
#     data = serializers.serialize("json", [book, ])
#     return HttpResponse(data, content_type="application/json")
