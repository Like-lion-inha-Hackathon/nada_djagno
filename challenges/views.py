from django.shortcuts import render

# Create your views here.


def challenge_view(request):
    return render(request, "challenge/challenge.html")


def challenge_study_view(request):
    return render(request, "challenge/challenge_study.html")


def challenge_reading_view(request):
    return render(request, "challenge/challenge_reading.html")


def write_challenge_view(request):
    return render(request, "challenge/write_challenge.html")
