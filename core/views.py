from django.shortcuts import render
from django.core import serializers
import json
from users import models as user_models
from django.http import JsonResponse

# Create your views here.


def intro_view(request):
    return render(request, "intro.html")


def try_view(request):
    if request.GET:
        return render(request, "try.html")

    users = user_models.User.objects.all()
    user_list = []
    for user in users:
        user_dict = {"id": user.id, "name": user.nickname}
        user_list.append(user_dict)

    return JsonResponse({"user_list": user_list})
