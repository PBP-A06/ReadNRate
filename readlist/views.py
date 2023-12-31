from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core import serializers
from .forms import AddBooksToReadlistForm
from .models import Readlist, Book
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#show all existing readlists
def show_readlist(request):
    top_5_readlists = Readlist.objects.all()

    context = {
        'top_5_readlists': top_5_readlists,
    }

    return render(request, 'readlist.html', context)

#get readlist details
def readlist_detail(request, readlist_id):
    readlist = get_object_or_404(Readlist, id=readlist_id)
    # return HttpResponse(serializers.serialize("json", readlist), content_type="application/json")
    return render(request, 'readlist_detail.html', {'readlist': readlist})

#TODO: make login required
@login_required(login_url='/login')
def create_readlist(request):
    if request.method == 'POST':
        form = AddBooksToReadlistForm(request.POST)
        if form.is_valid():
            readlist = form.save(commit=False)
            readlist.user = request.user
            readlist.save()
            form.save_m2m()  # This is needed to save the many-to-many relationship
            return JsonResponse({'status':'success', 'message':'Readlist created successfully'})
    else:
        form = AddBooksToReadlistForm()
    return render(request, 'create_readlist.html', {'form': form})

#TODO:fix likes
#increment number of likes
def like_a_readlist(request, id):
    updated_readlist = Readlist.objects.get(pk=id)
    updated_readlist.likes += 1
    updated_readlist.save()
    return HttpResponseRedirect(reverse('main:show_main'))

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
    return render(request, "leaderboard:details-book.html", context)

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
@login_required(login_url='/login')
def toggle_like_readlist(request, id):
    if request.method == 'POST':
        readlist = get_object_or_404(Readlist, pk=id)
        if request.user in readlist.liked_by.all():
            readlist.liked_by.remove(request.user)
            readlist.likes -= 1
        else:
            readlist.liked_by.add(request.user)
            readlist.likes += 1

        readlist.save()  # Tambahkan baris ini untuk menyimpan perubahan

        total_likes = readlist.liked_by.count()  # Menghitung jumlah like yang diperbarui
        has_liked = request.user in readlist.liked_by.all() if request.user.is_authenticated else False

        return JsonResponse({'status': 'success', 'total_likes': total_likes, 'has_liked': has_liked})
    
@csrf_exempt
def show_readlist_flutter(request, pk):
    readlist = Readlist.objects.filter(pk=pk)
    books = readlist.books.all()
    return HttpResponse(serializers.serialize("json", books), content_type="application/json") 