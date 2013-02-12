from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from accounts.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

