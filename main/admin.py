from django.contrib import admin
from .models import Book
from readlist.models import Readlist

admin.site.register(Book)
admin.site.register(Readlist)