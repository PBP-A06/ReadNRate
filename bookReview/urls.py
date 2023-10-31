from django.urls import path
from bookReview.views import *

app_name = "bookReview"  

urlpatterns = [
    path('book/<int:id>/', show_book_detail, name='book_detail'),
    path('add_review/<int:book_id>/', add_review_ajax, name='add_review'),
    path('path_to_your_api/', submit_review, name='submit_review'),
    path('toggle_bookmark/<int:id>/', toggle_bookmark, name='toggle_bookmark'),
    path('toggle_like/<int:id>/', toggle_like, name='toggle_like'),
]