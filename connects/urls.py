from django.urls import path
from . import views

urlpatterns = [
    path("", views.connect_view, name="main"),
]

app_name = "connects"
