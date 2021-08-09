from django.urls import path
from . import views

urlpatterns = [
    path("", views.challenge_view, name="main"),
    path("reading/<int:id>", views.challenge_reading_view, name="reading"),
    path("study/", views.challenge_study_view, name="study"),
    path("write/", views.write_challenge_view, name="write"),
]
app_name = "challenges"
