from django.shortcuts import render

# Create your views here.
def show_home(request):
<<<<<<< HEAD
    context = {}
    return render(request, "home.html", context)
=======
    context = {
        'nama': 'test'
    }
    return render(request, "home.html" , context)

>>>>>>> 6a1c430d01e2a239e09ffe14e7815a9c2d29f0be
