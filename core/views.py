from django.shortcuts import render
import json
from users import models as user_models

# Create your views here.


def intro_view(request):
    return render(request, "intro.html")


def try_view(request):
    users = user_models.User.objects.all()
    users = json.dumps(list(users))
    return render(request, "try.html", {"users": users})
