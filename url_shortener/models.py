from django.conf import settings
from django.db import models


# Create your models here.
class UrlMappingTable(models.Model):
    id = models.CharField(max_length=settings.URL_LENGTH, primary_key=True, unique=True)
    url = models.TextField()
