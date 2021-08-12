from django.db import models
from core import models as core_models
from users import models as user_models

# Create your models here.


class Record(core_models.TimeStampedModel):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50, null=True, blank=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    detail = models.TextField()
    thumbnail = models.ImageField(default=True)
