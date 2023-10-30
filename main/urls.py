from django.urls import path, include
from main.views import *

app_name = 'main'

urlpatterns = [
<<<<<<< HEAD
    path('', show_main, name="show_main"),
=======
>>>>>>> 6a1c430d01e2a239e09ffe14e7815a9c2d29f0be
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]