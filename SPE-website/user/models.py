from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='foobar', on_delete=models.CASCADE)
    institute_registration_number = models.CharField(max_length=20, null=True, blank=True)
    SPE_ID = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f'{self.user} Profile'

