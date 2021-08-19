from django.shortcuts import render
from records import models as record_models
from challenges import models as challenge_models
import json

# Create your views here.


def portfolio_view(request):
    age = 22
    ages = [
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
    ]
    data = [
        "3",
        "-1",
        "5",
        "7",
        "-4",
        "-1",
    ]
    text = [
        "인생 친구를 만남",
        "지리 올림피아드 은상",
        "인하대 합격",
        "고교 멘토링 활동",
        "군 입대",
        "군 전역",
    ]
    if request.POST:
        age += 1
        ages.append(str(age))
        text.append(str(request.POST.get("text1", "")))
        data.append(str(request.POST.get("number1", "0")))
    print(ages, data, text)
    data = json.dumps({"data": data})
    text = json.dumps({"text": text})
    ages = json.dumps({"ages": ages})

    records = record_models.Record.objects.all().order_by("start_date")
    # records = (
    #     record_models.Record.objects.all()
    #     .values_list("title", "start_date", "end_date")
    #     .union(
    #         challenge_models.Challenge.objects.all().values_list(
    #             "title", "start_date", "end_date"
    #         )
    #     )
    # )

    return render(
        request,
        "portfolio/portfolio.html",
        {"data": data, "text": text, "records": records, "ages": ages, "age": age},
    )


def portfolio_dohee_view(request):
    return render(request, "portfolio/portfolio_dohee.html")


def portfolio_compare_view(request):
    records = record_models.Record.objects.all()
    year = []
    for record in records:
        year.append(record.start_date.year)

    years = sorted(list(set(year)))
    return render(
        request,
        "portfolio/portfolio_compare.html",
        {"years": years, "records": records},
    )
