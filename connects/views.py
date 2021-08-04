from django.shortcuts import render

# Create your views here.


def connect_view(request):
    return render(request, "connect/connect.html")


def connect_dream_view(request):
    return render(request, "connect/connect_dream.html")


def connect_challenge_view(request):
    return render(request, "connect/connect_challenge.html")
