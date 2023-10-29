from django.urls import path
from home.views import *

urlpatterns = [
    path('', show_home, name='show_home'),
]