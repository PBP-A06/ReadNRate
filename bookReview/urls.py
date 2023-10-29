from django.urls import path
from bookReview.views import *

app_name = "bookReview"  

urlpatterns = [
    path('', show_book_detail, name='show_book_detail'),
    path('add_review/<int:book_id>/', add_review_ajax, name='add_review'),
    path('path_to_your_api/', submit_review, name='submit_review'),
    path('toggle_bookmark/', toggle_bookmark, name='toggle_bookmark'),
    path('toggle_like/', toggle_like, name='toggle_like'),
    # path('book_json/<int:id>/', get_books_by_id, name='show_json_by_id'),
]
