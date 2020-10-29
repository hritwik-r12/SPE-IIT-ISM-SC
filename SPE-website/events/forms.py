from django import forms
from django.contrib.auth.models import User
from .models import Registeration, SingleRegistration, Events
import datetime


# !!!!!!IMPORTANT!!!!!!!
# positively update event queryset before 2040, or the code will break

class RegisterForm(forms.ModelForm):
    date_1 = datetime.date.today()
    # below query set filters objects, if reg_date > today, displays the event form, else, doesn't.
    event = forms.ModelChoiceField(
        queryset=Events.objects.filter(reg_date__lte=datetime.date(2040, 1, 1), reg_date__gte=date_1))

    class Meta:
        model = Registeration
        fields = ['event', 'team_name', 'Member_1', 'Mobile_number', 'email', 'Member_2', 'Member_3', 'Member_4']


class SingleRegisterForm(forms.ModelForm):
    date_1 = datetime.date.today()
    event = forms.ModelChoiceField(
        queryset=Events.objects.filter(reg_date__lte=datetime.date(2040, 1, 1), reg_date__gte=date_1))

    class Meta:
        model = SingleRegistration
        fields = ['event', 'Member_1', 'Mobile_number', 'email']
