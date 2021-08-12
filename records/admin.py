from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ["title", "start_date", "end_date", "detail", "category"]
    pass
