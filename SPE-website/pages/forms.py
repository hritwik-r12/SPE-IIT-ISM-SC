# from django import forms
# from django.contrib.auth.models import User
# from .models import Profile


# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()
#     spe_id = forms.IntegerField(required=False)
#     IIT_ISM_registration_number = forms.CharField(required=False)
#
#     class Meta:
#         model = User
#         fields = ['email', 'spe_id', 'IIT_ISM_registration_number']
#
#
# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         pass
from django import forms
from .models import MessagesForUs

class MessagesForUsForm(forms.ModelForm):
    class Meta:
        model = MessagesForUs
        fields = ('sender', 'sender_email', 'message')
        labels = {
            'sender': 'Your name',
            'sender_email': 'Your email',
        }