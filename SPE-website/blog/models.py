from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images')
    date_posted = models.DateTimeField(default=timezone.now)
    overview = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title
