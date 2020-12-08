from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


'''class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()
    spe_id = forms.IntegerField(required=False)
    IIT_ISM_registration_number = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'spe_id', 'IIT_ISM_registration_number', 'password1', 'password2']'''

class CreateUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)
    spe_id = forms.CharField(required=False, label="SPE-ID")
    IIT_ISM_registration_number=forms.CharField(required=False, label="IIT (ISM) registration number")

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]