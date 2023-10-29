from django.urls import path, include
from main.views import *

urlpatterns = [
    path('', show_main, name="show_main"),
]