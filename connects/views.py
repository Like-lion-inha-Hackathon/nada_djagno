from django.shortcuts import render

# Create your views here.


def connect_view(request):
    cld = {}
    cloud = request.GET.get("cloud", "health")
    cld["cloud"] = cloud
    print(cloud)
    return render(request, "connect/connect.html", cld)


def connect_dream_view(request):
    return render(request, "connect/connect_dream.html")


def connect_challenge_view(request):
    return render(request, "connect/connect_challenge.html")
