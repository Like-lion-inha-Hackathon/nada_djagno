from django.shortcuts import render
from records import models as record_models
from challenges import models as challenge_models
import json

# Create your views here.


def portfolio_view(request):
    data = {}
    text = [
        "인생 친구를 만남",
        "지리 올림피아드 은상",
        "인하대 합격",
        "고교 멘토링 활동",
        "군 입대",
        "군 전역",
        "",
        "",
        "",
        "",
    ]
    if request.POST:
        text = []
        data = {}
        data["username"] = request.POST.get("username", "김연경")
        for i in range(1, 11):
            data[f"num{i}"] = request.POST.get(f"number{i}", "0")
            text.append(request.POST.get(f"text{i}", ""))
    else:
        data = {
            "username": "김연경",
            "num1": "3",
            "num2": "-1",
            "num3": "5",
            "num4": "7",
            "num5": "-4",
            "num6": "-1",
            "num7": "",
            "num8": "",
            "num9": "",
            "num10": "",
        }
        # for i in range(1, 10):
        #     data[f"{i}"] = "0"
    data = json.dumps({"data": [data]})
    text = json.dumps({"text": text})

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
        {"data": data, "text": text, "records": records},
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
