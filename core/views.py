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
    if request.POST:
        data["username"] = request.POST.get("username")
        for i in range(1, len(request.POST) - 1):
            data[f"num{i}"] = request.POST.get(f"number{i}", "0")
        print(data)
        data = json.dumps({"user": [data]})
    return render(request, "try.html", {"user": data})


def json_data_view(request):

    users = user_models.User.objects.all()
    user_list = []
    for user in users:
        user_dict = {"id": user.id, "name": user.nickname}
        user_list.append(user_dict)

    return JsonResponse({"user_list": user_list})
