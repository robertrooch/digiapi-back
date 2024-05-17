from django.db import models
from django.conf import settings

class Link(models.Model):
    nombre = models.TextField(blank=True)
    tipo = models.TextField(blank=True)
    nivel = models.TextField(blank=True)
    image = models.URLField(blank=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    link = models.ForeignKey('Links.Link', related_name='votes', on_delete=models.CASCADE)
