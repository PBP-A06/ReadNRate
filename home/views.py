from django.shortcuts import render

# Create your views here.
def show_home(request):
    context = {
        'nama': 'test'
    }
    return render(request, "home.html" , context)