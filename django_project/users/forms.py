from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import Profile

class UserRegisterForm(UserChangeForm):
    password = None
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        # fields = ["username", "email", "password1", "passwors2"]
        fields = ["username", "email"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]
