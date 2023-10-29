from django.shortcuts import render

# Create your views here.
def show_home(request):
<<<<<<< HEAD
    context = {
        'nama': 'test'
    }
    return render(request, "home.html" , context)

=======
    context = {}
    return render(request, "home.html", context)
>>>>>>> 3681b6b7580e7496faf1b843585938f67b80d8e8
