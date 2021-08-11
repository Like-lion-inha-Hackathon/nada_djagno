from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from . import models as record_models
import random

# Create your views here.


def records_view(request):
    page = int(request.GET.get("page", 1) or 1)
    queryset = (
        record_models.Record.objects.filter(category="licence")
        | record_models.Record.objects.filter(category="language")
        | record_models.Record.objects.filter(category="grade")
        | record_models.Record.objects.filter(category="internship")
        | record_models.Record.objects.filter(category="volunteer")
        | record_models.Record.objects.filter(category="work")
    )
    queryset.order_by("created")
    records = record_models.Record.objects.get_queryset().order_by("id")
    paginator = Paginator(records, 6)
    records = paginator.get_page(page)
    return render(
        request, "records/records.html", {"queryset": queryset, "records": records}
    )


def records_write_view(request):
    if request.POST:
        title = request.POST.get("title")
        period = request.POST.get("period")
        category = request.POST.get("category")
        detail = request.POST.get("detail")
        random_number = random.randint(1, 6)
        thumbnail = f"records/record_{random_number}.png"
        record_models.Record.objects.create(
            title=title,
            period=period,
            category=category,
            detail=detail,
            thumbnail=thumbnail,
        )
        return redirect("records:main")

    return render(request, "records/records_write.html")


def records_calender_view(request):
    return render(request, "records/records_calender.html")


def records_write_scrap_view(request):
    return render(request, "records/records_write_scrap.html")
