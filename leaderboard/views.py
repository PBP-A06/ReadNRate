from django.shortcuts import render
from book.models import Book
from leaderboard.models import RatingLeaderboardEntry
from readlist.models import Readlist
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from leaderboard.forms import SearchForm 

@csrf_exempt
def leaderboard_option(request):
    books = Book.objects.all().order_by('title')
    book = books[0]
    form = SearchForm(request.POST or None)
    counter = 1

    if request.method == "POST":
        selected_title = request.POST.get('select')
        books = books.order_by('-stars', 'title')
        counter = 0
        for b in books:
            counter += 1
            if b.title == selected_title:
                book = b
                break
        book = Book.objects.filter(title=selected_title)[0]

    context = {
        'books':books,
        'book':book,
        'form':form,
        'rank':counter,
    }
    return render(request, "leaderboard.html", context)

@csrf_exempt
def get_books(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def show_book_by_id(request, pk):
    book = Book.objects.filter(pk=pk)[0]
    context = {
        'book':book,
    }
    return render(request, "details-book.html", context)

@csrf_exempt
def get_readlists(request):
    readlists = Readlist.objects.all()
    return HttpResponse(serializers.serialize("json", readlists), content_type="application/json") 

@csrf_exempt
def show_readlist_by_id(request, pk):
    readlist = Readlist.objects.filter(pk=pk)[0]
    books = readlist.books.all()
    context = {
        'readlist':readlist,
        'books':books,
    }
    return render(request, "details-readlist.html", context)

@csrf_exempt
def create_leaderboard_entries(request):
    books = Book.objects.all().order_by('-stars', 'title')
    leaderboard_entries = [RatingLeaderboardEntry(book=book) for book in books]
    RatingLeaderboardEntry.objects.bulk_create(leaderboard_entries)