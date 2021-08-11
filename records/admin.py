from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ["title", "period", "detail", "category"]
    pass
