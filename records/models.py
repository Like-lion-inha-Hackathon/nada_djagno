from django.db import models
from core import models as core_models
from users import models as user_models

# Create your models here.


class Record(core_models.TimeStampedModel):
    title = models.CharField(max_length=50)
    detail = models.TextField()
    author = models.ForeignKey(
        user_models.User, on_delete=models.CASCADE, null=True, blank=True
    )
