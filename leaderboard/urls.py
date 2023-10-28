from django.urls import path
from leaderboard.views import *

urlpatterns = [
    path('', leaderboad_option, name='leaderboad_option'),
    path('likes/', show_by_likes, name='show_by_likes'),
    path('rating/', show_by_rating, name='show_by_rating'),
    path('readlist/', show_readlist, name='show_readlist'),
]