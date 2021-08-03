from django import forms
from django.db.models import fields
from django.forms import widgets
from . import models


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "email", "nickname")
        widgets = {
            "first_name": widgets.TextInput(attrs={"class": "first_name"}),
            "last_name": widgets.TextInput(attrs={"class": "last_name"}),
            "email": widgets.EmailInput(attrs={"class": "email"}),
            "nickname": widgets.TextInput(attrs={"class": "nickname"}),
        }
        labels = {
            "first_name": "First_name",
            "last_name": "Last_name",
            "email": "Email",
        }
        help_texts = {"username": None}

    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError("패스워드를 정확하게 입력하세요")
        else:
            return password

    def save(self):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user.email = email
        user.username = email
        user.set_password(password)
        user.save()


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(username=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", "Password is Wrong")
        except models.User.DoesNotExist:
            self.add_error("email", "User does not exist")
