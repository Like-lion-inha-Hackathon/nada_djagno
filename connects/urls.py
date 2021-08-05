from django.urls import path
from . import views

urlpatterns = [
    path("", views.connect_view, name="main"),
    path("dream/", views.connect_dream_view, name="dream"),
    path("challenge/", views.connect_challenge_view, name="challenge"),
]

app_name = "connects"
