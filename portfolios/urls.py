from django.urls import path
from . import views

urlpatterns = [
    path("", views.portfolio_view, name="main"),
    path("dehee/", views.portfolio_dohee_view, name="dohee"),
]

app_name = "portfolios"
