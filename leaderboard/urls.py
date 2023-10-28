from django.urls import path
from leaderboard.views import *
# from django.contrib import admin

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', leaderboad_option, name='leaderboad_option'),
]