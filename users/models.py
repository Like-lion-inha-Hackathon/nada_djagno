from django.db import models
from django.contrib.auth.models import AbstractUser
from core import models as core_models


class User(AbstractUser):
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )
    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    bio = models.TextField(default="", blank=True)
    nickname = models.CharField(max_length=30)
    birthdate = models.DateField(blank=True, null=True)
    superhost = models.BooleanField(default=False)


class Guest(core_models.TimeStampedModel):
    username = models.CharField(max_length=50)
