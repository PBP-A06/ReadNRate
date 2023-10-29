from django.urls import path, include
from main.views import *

urlpatterns = [
    path('', show_main, name="show_main"),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]