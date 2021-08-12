from django.urls import path
from . import views

urlpatterns = [
    path("", views.portfolio_view, name="main"),
    path("dehee/", views.portfolio_dohee_view, name="dohee"),
    path("compare/", views.portfolio_compare_view, name="compare"),
]

app_name = "portfolios"
