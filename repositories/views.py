from django.shortcuts import render

# Create your views here.


def repository_view(request):
    return render(request, "repository/repository.html")
