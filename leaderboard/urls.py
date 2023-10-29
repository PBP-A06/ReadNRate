from django.urls import path
from leaderboard.views import *
# from django.contrib import admin

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', leaderboard_option, name='leaderboard_option'),
    path("get-books", get_books, name="get_books")
    # path("get-readlists", get_readlists, name="get_readlists")
]