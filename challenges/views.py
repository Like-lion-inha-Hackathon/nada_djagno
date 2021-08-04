from django.shortcuts import render

# Create your views here.


def challenge_view(request):
    return render(request, "challenge/challenge.html")
