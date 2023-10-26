from django.shortcuts import render

# Create your views here.
def show_main(request):

    context = {
        'test':'testing'
    }

    return render(request, "main.html", context)