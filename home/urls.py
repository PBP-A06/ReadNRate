from django.urls import path
from home.views import *

app_name = 'home'

urlpatterns = [
<<<<<<< HEAD
    path('', show_home, name='show_home'),
=======
    path('', show_home, name = 'show_home'),
>>>>>>> 6a1c430d01e2a239e09ffe14e7815a9c2d29f0be
]