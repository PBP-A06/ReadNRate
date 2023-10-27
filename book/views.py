from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from book.models import Book

def get_books(request):
    data = Book.objects.all()
    data_json = serializers.serialize("json", data)
    return HttpResponse(data_json, content_type="application/json")