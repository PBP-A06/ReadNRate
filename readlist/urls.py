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
    #  path('redirect/', redirect_to_other_app, name='redirect'),
    # path('readlist_detail/<int:readlist_id>', readlist_detail, name='readlist_detail'),
]