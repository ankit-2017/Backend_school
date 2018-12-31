

from django.db import models



class django_title(models.Model):
    title = models.CharField(max_length=250)
    url = models.CharField(max_length=100, blank=True, null=True)
    dat = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class django_url(models.Model):
    url = models.CharField(max_length=100)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name