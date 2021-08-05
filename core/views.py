from django.shortcuts import render

# Create your views here.


def intro_view(request):
    return render(request, "intro.html")


def try_view(request):
    return render(request, "try.html")
