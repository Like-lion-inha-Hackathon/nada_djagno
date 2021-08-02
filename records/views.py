from django.shortcuts import render

# Create your views here.
def records_view(request):
    return render(request, "records/records.html")


def portfolio_view(request):
    return render(request, "portfolio/portfolio.html")


def challenge_view(request):
    return render(request, "challenge/challenge.html")


def connect_view(request):
    return render(request, "connect/connect.html")


def repository_view(request):
    return render(request, "repository/repository.html")
