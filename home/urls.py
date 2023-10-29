from django.urls import path, include
from home.views import *

urlpatterns = [
    path('', show_home, name = 'show_home'),
]