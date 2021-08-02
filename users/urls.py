from django.urls import path
from . import views

urlpatterns = [
    path("", views.IntroView.as_view(), name="intro"),
    path("main/", views.MainView.as_view(), name="main"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.log_out, name="logout"),
]

app_name = "users"
