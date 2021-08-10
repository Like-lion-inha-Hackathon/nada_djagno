from django.shortcuts import render
from django.core import serializers
import json
from users import models as user_models
from django.http import JsonResponse

# Create your views here.


def intro_view(request):
    return render(request, "intro.html")


def try_view(request):
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
        data["username"] = request.POST.get("username")
        for i in range(1, 11):
            data[f"num{i}"] = request.POST.get(f"number{i}", "0")
            text.append(request.POST.get(f"text{i}", ""))
    else:
        for i in range(1, 10):
            data[f"{i}"] = "0"
    data = json.dumps({"user": [data]})
    text = json.dumps({"text": text})
    return render(request, "try.html", {"user": data, "text": text})


def json_data_view(request):

    users = user_models.User.objects.all()
    user_list = []
    for user in users:
        user_dict = {"id": user.id, "name": user.nickname}
        user_list.append(user_dict)

    return JsonResponse({"user_list": user_list})
