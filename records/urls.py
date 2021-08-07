from django.urls import path
from . import views

urlpatterns = [
    path("", views.records_view, name="main"),
    path("", views.records_write_view, name="write"),
    path("", views.records_calender_view, name="calender"),
]

app_name = "records"
