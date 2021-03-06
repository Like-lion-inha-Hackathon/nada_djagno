from django.contrib import admin
from . import models as challenge_models

# Register your models here.
@admin.register(challenge_models.Challenge)
class ChallegeAmdin(admin.ModelAdmin):
    list_display = [
        "title",
        "start_date",
        "end_date",
        "detail",
        "category",
    ]
    pass
