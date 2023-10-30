from django.shortcuts import render

<<<<<<< HEAD
# Create your views here.
=======

# Create your views here.
def show_books(request):
    context = {
        'nama': 'test'
    }
    return render(request, "books.html" , context)

# Create your views here.

>>>>>>> 6a1c430d01e2a239e09ffe14e7815a9c2d29f0be
