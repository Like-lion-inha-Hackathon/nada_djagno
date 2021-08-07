from django.shortcuts import render

# Create your views here.


def repository_view(request):
    return render(request, "repository/repository.html")


def repository_portfolio_view(request):
    return render(request, "repository/repositoryportfolio.html")
