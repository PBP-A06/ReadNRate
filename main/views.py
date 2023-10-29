from django.shortcuts import render
<<<<<<< HEAD
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
=======
from book.models import Book
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
>>>>>>> 3681b6b7580e7496faf1b843585938f67b80d8e8

@csrf_exempt
def show_main(request):
    books = Book.objects.all()
    context = {
        'books':books,
    }
<<<<<<< HEAD

    return render(request, "main.html", context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
=======
    return render(request, "main.html", context)
>>>>>>> 3681b6b7580e7496faf1b843585938f67b80d8e8
