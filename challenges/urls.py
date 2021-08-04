from django.urls import path
from . import views

urlpatterns = [
    path("", views.challenge_view, name="main"),
]

app_name = "challenges"
