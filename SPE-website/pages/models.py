from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

class MessagesForUs(models.Model):
    sender = models.CharField(max_length=100)
    sender_email = models.CharField(max_length=120)
    message = models.CharField(max_length=600)