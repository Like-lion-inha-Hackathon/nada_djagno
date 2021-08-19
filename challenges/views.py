from django.shortcuts import redirect, render
from . import models as challenge_models
import random
import datetime

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
    period = challenge.end_date - challenge.start_date
    period = range(period.days + 1)
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
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        detail = request.POST.get("detail")
        category = request.POST.get("category")
        random_number = random.randint(1, 3)
        thumbnail = f"challenge/{category}/{category}_{random_number}.png"
        startyear, startmonth, startday = (
            int(start_date[:4]),
            int(start_date[5:7]),
            int(start_date[8:10]),
        )
        start_date = datetime.date(startyear, startmonth, startday)
        endyear, endmonth, endday = (
            int(end_date[:4]),
            int(end_date[5:7]),
            int(end_date[8:10]),
        )
        end_date = datetime.date(endyear, endmonth, endday)
        period = end_date - start_date
        challenge = challenge_models.Challenge.objects.create(
            title=title,
            start_date=start_date,
            end_date=end_date,
            detail=detail,
            category=category,
            thumbnail=thumbnail,
        )

        return redirect("challenges:main")
    return render(request, "challenge/write_challenge.html", content)
