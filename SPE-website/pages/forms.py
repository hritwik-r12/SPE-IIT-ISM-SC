from django import forms
from .models import MessagesForUs

class MessagesForUsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update(style='height: 20em')

    class Meta:
        model = MessagesForUs
        fields = ('sender', 'sender_email', 'message')
        labels = {
            'sender': 'Your name',
            'sender_email': 'Your email',
        }
        