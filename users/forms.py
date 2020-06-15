from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserUpdateForm(forms.Form):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class UserProfileModel(forms.Form):
    class Meta:
        model = Profile
        fields = ['image']
