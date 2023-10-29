from django.urls import path
from readlist.views import *

app_name = 'readlist'

urlpatterns = [
    path('', show_readlist, name='show_readlist'),
    path('create_readlist/', create_readlist, name='create_readlist'),
    path('readlist_detail/<int:readlist_id>', readlist_detail, name='readlist_detail'),
]