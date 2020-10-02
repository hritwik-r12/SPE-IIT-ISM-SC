from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Events(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    reg_date = models.DateField()
    content = models.TextField()
    image = models.ImageField(null=True, blank=True,upload_to='event_poster')
    google_doc_url = models.URLField(max_length=500)

    def __str__(self):
        return self.title

    @property
    def has_happened(self):
        t = date.today()
        return t > self.reg_date

class Registeration(models.Model):
    event= models.ForeignKey(Events, on_delete=models.CASCADE)
    first_user = models.OneToOneField(User, on_delete=models.CASCADE)
    user2 = models.CharField(max_length=300,null=True, blank=True)
    user3 = models.CharField(max_length=300,null=True, blank=True)
    user4 = models.CharField(max_length=300,null=True, blank=True)
    phone = models.IntegerField()
    email = models.EmailField(max_length=200)
    team_name= models.CharField(max_length=300,null=True, blank=True)

    def __str__(self):
        return f'{self.first_user.username} regestration'