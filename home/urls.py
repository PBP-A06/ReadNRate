from django.urls import path, include
from home.views import *

app_name = 'home'

urlpatterns = [
    path('', show_home, name = 'show_home'),
]