from django import forms
from django.contrib.auth.models import User
from .models import Registeration

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Registeration
        fields=['first_user','user2','user3','user4','phone','email','team_name']