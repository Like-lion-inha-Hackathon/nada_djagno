from django.shortcuts import render

# Create your views here.


def portfolio_view(request):
    return render(request, "portfolio/portfolio.html")


def portfolio_dohee_view(request):
    return render(request, "portfolio/portfolio_dohee.html")
