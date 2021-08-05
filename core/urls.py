from django.urls import path
from . import views

urlpatterns = [
    path("", views.intro_view, name="intro"),
    path("try/", views.try_view, name="try"),
]

app_name = "core"
