from django.db import models


class Events(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    reg_date = models.DateField()
    content = models.TextField()
    image = models.ImageField(null=True, blank=True,upload_to='event_poster')
    google_doc_url = models.URLField(max_length=500)

    def __str__(self):
        return self.title
