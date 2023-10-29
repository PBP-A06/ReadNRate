from django.urls import path, include
from main.views import *

urlpatterns = [
    path('', include('home.urls')),
]