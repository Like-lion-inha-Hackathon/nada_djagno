from django.db import models
from core import models as core_models

# Create your models here.
class Challenge(core_models.TimeStampedModel):
    CATEGORY_CHOICES = (
        ("study", "Study"),
        ("reading", "Reading"),
        ("hobby", "Hobby"),
        ("health", "Health"),
        ("habbit", "Habbit"),
        ("work", "Work"),
    )
    title = models.CharField(max_length=50)
    period = models.IntegerField(null=True, default=0)
    method = models.TextField(null=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, null=True)
