from django import forms
from django.contrib.auth.models import User
import re


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=255, label="Tai khoan", required=True)
    email = forms.EmailField(label="Email", required=True)
    password1 = forms.CharField(
        max_length=255,
        label="Mat khau",
        widget=forms.PasswordInput,
        required=True,
    )
    password2 = forms.CharField(
        max_length=255,
        label="Nhap lai mat khau",
        widget=forms.PasswordInput,
        required=True,
    )

    def clean_password2(self):
        if "password1" in self.cleaned_data:
            password1 = self.cleaned_data["password1"]
            password2 = self.cleaned_data["password2"]
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Mat khau khong hop le")

    def clean_username(self):
        username = self.cleaned_data["username"]
        if not re.search(r"^[A-Za-z0-9]+(?:[ _-][A-Za-z0-9]+)*$", username):
            raise forms.ValidationError("User ko hop le")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("User da ton tai")

    def save(self):
        User.objects.create_user(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["email"],
            password=self.cleaned_data["password1"],
            # is_staff = True,
        )