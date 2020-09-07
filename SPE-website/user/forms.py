from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()
    spe_id = forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'spe_id', 'password1', 'password2']