from django.urls import path
from . import views

urlpatterns = [
    path("", views.portfolio_view, name="main"),
]

app_name = "portfolios"
