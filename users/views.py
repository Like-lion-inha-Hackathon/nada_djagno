from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import ListView, FormView
from django.contrib.auth import login, logout, authenticate
from . import models
from . import forms

# Create your views here.


class MainView(ListView):
    model = models.User
    template_name = "main.html"


class IntroView(ListView):
    model = models.User
    template_name = "intro.html"


def signup_view(request):
    res_data = {}
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = models.User.objects.create_user(
                username=request.POST["username"],
                email=request.POST["email"],
                password=request.POST["password1"],
            )
            login(request, user)
            return redirect("/")
        else:
            res_data["error"] = "비밀번호가 다릅니다."
    return render(request, "users/signup.html", res_data)


def login_view(request):
    res_data = {}
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect("/")
        else:
            res_data["error"] = "아이디나 비밀번호가 틀렸어요~"
    return render(request, "users/login.html", res_data)


class SignUpView(FormView):
    template_name = "users/signup.html"
    success_url = reverse_lazy("users:main")
    form_class = forms.SignUpForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(FormView):
    template_name = "users/login.html"
    success_url = reverse_lazy("users:main")
    form_class = forms.LoginForm

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(username=email, email=email, password=password)
        if user is not None:
            login(self.request, user)
            print("login")
        return super().form_valid(form)


def log_out(request):
    logout(request)
    return redirect(reverse(("users:main")))
