from django.shortcuts import render

# Create your views here.
def records_view(request):
    return render(request, "records/records.html")


def records_write_view(request):
    return render(request, "records/records_write.html")


def records_calender_view(request):
    return render(request, "records/records_calender.html")
