from django.db import models
from core import models as core_models

# Create your models here.
class Challenge(core_models.TimeStampedModel):
    title = models.CharField(max_length=50)
    period = models.IntegerField(null=True, default=0)
    method = models.TextField(null=True)
