from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Events(models.Model):
    objects = None
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    reg_date = models.DateField()
    content = models.TextField()
    google_doc_url = models.URLField(max_length=500)
    img_url = models.URLField()

    def __str__(self):
        return self.title

    @property
    def has_happened(self):
        t = date.today()
        return t > self.reg_date


class Registeration(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=300, null=True, blank=True)
    Member_1 = models.CharField(max_length=300)
    Mobile_number = models.IntegerField()
    email = models.EmailField(max_length=200)
    Member_2 = models.CharField(max_length=300, null=True, blank=True)
    Member_3 = models.CharField(max_length=300, null=True, blank=True)
    Member_4 = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f'{self.Member_1} {self.event.title} regestration'


class SingleRegistration(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    Member_1 = models.CharField(max_length=100)
    Mobile_number = models.IntegerField()
    email = models.EmailField(max_length=200)

    def __str__(self):
        return f'{self.Member_1} {self.event.title} single registration'
