from django import forms
from django.contrib.auth.models import User
from .models import Registeration

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Registeration
        fields=['event','team_name','Member_1','Mobile_number','email','Member_2','Member_3','Member_4']