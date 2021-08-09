from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "User Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "superhost",
                    "nickname",
                ),
            },
        ),
    )
    list_display = [
        "username",
        "nickname",
        "email",
        "gender",
        "birthdate",
        "superhost",
    ]


@admin.register(models.Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = [
        "username",
    ]
