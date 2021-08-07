from django.shortcuts import render
from django.core import serializers
import json
from users import models as user_models

# Create your views here.


def intro_view(request):
    return render(request, "intro.html")


def try_view(request):
    users = user_models.User.objects.all()
    users = serializers.serialize("json", users)

    return render(request, "try.html", {"users": users})
