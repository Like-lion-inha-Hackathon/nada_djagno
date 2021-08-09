from django.urls import path
from . import views

urlpatterns = [
    path("", views.repository_view, name="main"),
    path("portfolio/", views.repository_portfolio_view, name="portfolio"),
]

app_name = "repositories"
