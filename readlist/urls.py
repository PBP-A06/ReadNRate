from django.urls import path
from readlist.views import *
from leaderboard.views import show_readlist_by_id

app_name = 'readlist'

urlpatterns = [
    path('', show_readlist, name='show_readlist'),
    path('create-readlist/', create_readlist, name='create_readlist'),
    path("readlist-id-<int:pk>/", show_readlist_by_id, name="show_readlist_by_id"),
    path("get-readlists/", get_readlists, name="get_readlists"),
    path("get-books/", get_books, name="get_books"),
    path('toggle_like_readlist/<int:id>/', toggle_like_readlist, name='toggle_like_readlist'),
    path("readlist-flutter/<int:pk>/", show_readlist_flutter, name="show_readlist_flutter"),
]