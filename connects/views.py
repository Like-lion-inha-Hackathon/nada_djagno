from django.shortcuts import render

# Create your views here.


def connect_view(request):
    return render(request, "connect/connect.html")
