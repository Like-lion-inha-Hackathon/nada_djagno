from django.shortcuts import redirect, render
from . import models as challenge_models
import random

# Create your views here.


def challenge_view(request):
    if request.GET:
        print("GET")
    challenges = challenge_models.Challenge.objects.all()
    return render(request, "challenge/challenge.html", {"challenges": challenges})


def challenge_tag_view(request, tag):
    context = {}
    if tag == "all":
        all = challenge_models.Challenge.objects.all()
        context["all"] = all
    elif tag == "study":
        all = challenge_models.Challenge.objects.filter(category=tag)
        context["all"] = all
    elif tag == "habbit":
        all = challenge_models.Challenge.objects.filter(category=tag)
        context["all"] = all
    elif tag == "reading":
        all = challenge_models.Challenge.objects.filter(category=tag)
        context["all"] = all
    elif tag == "hobby":
        all = challenge_models.Challenge.objects.filter(category=tag)
        context["all"] = all
    elif tag == "work":
        all = challenge_models.Challenge.objects.filter(category=tag)
        context["all"] = all
    elif tag == "health":
        all = challenge_models.Challenge.objects.filter(category=tag)
        context["all"] = all

    return render(request, "challenge/challenge.html", context)


def challenge_study_view(request):
    return render(request, "challenge/challenge_study.html")


def challenge_reading_view(request, id):
    challenge = challenge_models.Challenge.objects.get(pk=id)
    challenges = challenge_models.Challenge.objects.all()
    period = range(challenge.period)
    return render(
        request,
        "challenge/challenge_reading.html",
        {"challenge": challenge, "period": period},
    )


def write_challenge_view(request):

    content = {}
    if request.POST:
        print("post")
        title = request.POST.get("title")
        period = int(request.POST.get("period"))
        method = request.POST.get("method")
        category = request.POST.get("category")
        random_number = random.randint(1, 3)
        thumbnail = f"challenge/{category}/{category}_{random_number}.png"
        challenge = challenge_models.Challenge.objects.create(
            title=title,
            period=period,
            method=method,
            category=category,
            thumbnail=thumbnail,
        )

        return redirect("challenges:main")
    return render(request, "challenge/write_challenge.html", content)
