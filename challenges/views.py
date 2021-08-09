from django.shortcuts import redirect, render
from . import models as challenge_models

# Create your views here.


def challenge_view(request):
    challenges = challenge_models.Challenge.objects.all()
    return render(request, "challenge/challenge.html", {"challenges": challenges})


def challenge_study_view(request):
    return render(request, "challenge/challenge_study.html")


def challenge_reading_view(request, id):
    challenge = challenge_models.Challenge.objects.get(pk=id)
    challenges = challenge_models.Challenge.objects.all()
    print(len(challenges))
    return render(request, "challenge/challenge_reading.html", {"challenge": challenge})


def write_challenge_view(request):

    content = {}
    if request.POST:
        print("post")
        title = request.POST.get("title")
        period = int(request.POST.get("period"))
        method = request.POST.get("method")
        category = request.POST.get("category")
        challenge = challenge_models.Challenge.objects.create(
            title=title, period=period, method=method, category=category
        )
        print(challenge)

        return redirect("challenges:main")
    return render(request, "challenge/write_challenge.html", content)
