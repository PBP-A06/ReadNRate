from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .forms import AddBooksToReadlistForm
from .models import Readlist, Book
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

def show_readlist(request):
    top_5_readlists = Readlist.objects.all()

    context = {
        'top_5_readlists': top_5_readlists,
    }

    return render(request, 'readlist.html', context)

def readlist_detail(request, readlist_id):
    readlist = get_object_or_404(Readlist, id=readlist_id)
    return HttpResponse(serializers.serialize("json", readlist), content_type="application/json")
    # return render(request, 'readlist_detail.html', {'readlist': readlist})

# @login_required(login_url='/login')
def create_readlist(request):
    if request.method == 'POST':
        form = AddBooksToReadlistForm(request.POST)
        if form.is_valid():
            readlist = form.save(commit=False)
            readlist.user = request.user
            readlist.save()
            form.save_m2m()  # This is needed to save the many-to-many relationship
            return redirect('readlist:readlist_detail', pk=readlist.pk)
    else:
        form = AddBooksToReadlistForm()
    return render(request, 'create_readlist.html', {'form': form})


