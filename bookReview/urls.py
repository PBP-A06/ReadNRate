from django.urls import path
from bookReview.views import *

app_name = "book"  # Pastikan app_name mengacu pada aplikasi "book" Anda

urlpatterns = [
    path('', show_book_detail, name='show_book_detail'),
    path('add_review/<int:book_id>/', add_review, name='add_review'),
    # path('book_json/<int:id>/', get_books_by_id, name='show_json_by_id'),
]
