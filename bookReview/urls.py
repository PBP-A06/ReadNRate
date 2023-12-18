from django.urls import path
from bookReview.views import *

app_name = "bookReview"  

urlpatterns = [
    path('book/<int:id>/', show_book_detail, name='book_detail'),
    path('add_review/<int:id>/', add_review_ajax, name='add_review'),
    path('path_to_your_api/', submit_review, name='submit_review'),
    path('toggle_bookmark/<int:id>/', toggle_bookmark, name='toggle_bookmark'),
    path('toggle_like/<int:id>/', toggle_like, name='toggle_like'),
    path('get_reviews/<int:book_id>/', get_reviews, name='get_reviews'),
    path('get_reviews_all/', get_reviews_all, name='get_reviews_all'),
    path('get_like_status/<int:id>/', get_like_status, name='get_like_status'),
    path('get_bookmark_status/<int:id>/', get_bookmark_status, name='get_bookmark_status'),
    path('get_like_count/<int:id>/', get_like_count, name='get_like_count'),
]
