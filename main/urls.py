from django.urls import path, include
from main.views import *

urlpatterns = [
<<<<<<< HEAD
    path('', include('home.urls')),
    path('books/', include('books.urls')),
=======
    path('', show_main, name="show_main"),
>>>>>>> 3681b6b7580e7496faf1b843585938f67b80d8e8
]