from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from . import models as record_models
from challenges import models as challenge_models
import random
import datetime

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
    records = record_models.Record.objects.all().order_by("-updated")
    reco = record_models.Record.objects.all().filter(
        end_date__lte=datetime.datetime.now()
    )
    all = (
        challenge_models.Challenge.objects.all()
        .values_list("title", "thumbnail", "start_date", "updated")
        .union(reco.values_list("title", "thumbnail", "start_date", "updated"))
    )
    all = (
        all.values_list("title", "thumbnail", "start_date", "updated")
        .union(queryset.values_list("title", "thumbnail", "start_date", "updated"))
        .order_by("-updated")
    )
    p = Paginator(all, 6)
    all = p.get_page(page)
    return render(
        request,
        "records/records.html",
        {"queryset": queryset, "records": records, "all": all},
    )


def records_write_view(request):
    if request.POST:
        title = request.POST.get("title")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        category = request.POST.get("category")
        startyear, startmonth, startday = (
            int(start_date[:4]),
            int(start_date[5:7]),
            int(start_date[8:10]),
        )
        start_date = datetime.date(startyear, startmonth, startday)
        endyear, endmonth, endday = (
            int(end_date[:4]),
            int(end_date[5:7]),
            int(end_date[8:10]),
        )
        end_date = datetime.date(endyear, endmonth, endday)
        period = end_date - start_date
        detail = request.POST.get("detail")
        random_number = random.randint(1, 6)
        thumbnail = f"records/record_{random_number}.png"
        record_models.Record.objects.create(
            title=title,
            start_date=start_date,
            end_date=end_date,
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
