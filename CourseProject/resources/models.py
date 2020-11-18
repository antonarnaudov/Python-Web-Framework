from django.db import models


# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='public/images')
    passport = models.FileField(upload_to='private/documents')
