from distutils.command.upload import upload
from re import T
from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="")