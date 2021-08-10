from django.urls import path
from . import views

urlpatterns = [
    path("", views.records_view, name="main"),
    path("write/", views.records_write_view, name="write"),
    path("calender/", views.records_calender_view, name="calender"),
    path("scrap/", views.records_write_scrap_view, name="scrap"),
]
app_name = "records"
