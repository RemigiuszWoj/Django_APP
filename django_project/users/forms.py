from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class UserRegisterForm(UserChangeForm):
    password = None
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        # fields = ["username", "email", "password1", "passwors2"]
        fields = ["username", "email"]