from django.shortcuts import render
from . import models as challenge_models

# Create your views here.


def challenge_view(request):
    return render(request, "challenge/challenge.html")


def challenge_study_view(request):
    return render(request, "challenge/challenge_study.html")


def challenge_reading_view(request):
    return render(request, "challenge/challenge_reading.html")


def write_challenge_view(request):
    content = {}
    if request.POST:
        print("post")
        title = request.POST.get("title")
        period = int(request.POST.get("period"))
        method = request.POST.get("method")
        challenge = challenge_models.Challenge.objects.create(
            title=title, period=period, method=method
        )
        challenges = challenge_models.Challenge.objects.all()
        content = {
            "title": title,
            "period": period,
            "method": method,
            "challenges": challenges,
        }
    return render(request, "challenge/write_challenge.html", content)
