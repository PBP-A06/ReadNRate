from django.urls import path
from leaderboard.views import *
# from django.contrib import admin

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', leaderboard_option, name='leaderboard_option'),
    path("get-books/", get_books, name="get_books"),
    # path("book-id-<int:pk>/", show_book_by_id, name="show_book_by_id"),
    path("readlist-id-<int:pk>/", show_readlist_by_id, name="show_readlist_by_id"),
    path("get-readlists/", get_readlists, name="get_readlists"),
    path("get-100-best-rated-books/", get_100_best_rated_books, name="get_100_best_rated_books"),
    path("get-10-best-rated-books/", get_10_best_rated_books, name="get_10_best_rated_books"),
    path("get-100-most-liked-books/", get_100_most_liked_books, name="get_100_most_liked_books"),
    path("get-10-most-liked-books/", get_10_most_liked_books, name="get_10_most_liked_books"),
    path("get-100-books-sorted-by-title/", get_100_books_sorted_by_title, name="get_100_books_sorted_by_title"),
    path("get-100-books-sorted-by-category/", get_100_books_sorted_by_category, name="get_100_books_sorted_by_category"),
]