from django.shortcuts import render
import json

# Create your views here.


def portfolio_view(request):
    data = {}
    text = [
        "스물",
        "스물 하나",
        "스물 둘",
        "스물 셋",
        "스물 넷",
        "스물 다섯",
        "스물 여섯",
        "스물 일곱",
        "스물 여덟",
        "스물 아홉",
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
            "num1": "-2",
            "num2": "-4",
            "num3": "1",
            "num4": "3",
            "num5": "7",
            "num6": "9",
            "num7": "8",
            "num8": "5",
            "num9": "6",
            "num10": "10",
        }
        # for i in range(1, 10):
        #     data[f"{i}"] = "0"
    data = json.dumps({"data": [data]})
    text = json.dumps({"text": text})
    return render(request, "portfolio/portfolio.html", {"data": data, "text": text})


def portfolio_dohee_view(request):
    return render(request, "portfolio/portfolio_dohee.html")
