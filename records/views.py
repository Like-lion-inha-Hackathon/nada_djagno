from django.shortcuts import redirect, render
from . import models as record_models

# Create your views here.


def records_view(request):
    queryset = (
        record_models.Record.objects.filter(category="licence")
        | record_models.Record.objects.filter(category="language")
        | record_models.Record.objects.filter(category="grade")
        | record_models.Record.objects.filter(category="internship")
        | record_models.Record.objects.filter(category="volunteer")
        | record_models.Record.objects.filter(category="work")
    )
    queryset.order_by("created")
    print(queryset)
    return render(request, "records/records.html", {"queryset": queryset})


def records_write_view(request):
    if request.POST:
        title = request.POST.get("title")
        period = request.POST.get("period")
        category = request.POST.get("category")
        detail = request.POST.get("detail")
        record_models.Record.objects.create(
            title=title, period=period, category=category, detail=detail
        )
        return redirect("records:main")

    return render(request, "records/records_write.html")


def records_calender_view(request):
    return render(request, "records/records_calender.html")


def records_write_scrap_view(request):
    return render(request, "records/records_write_scrap.html")
