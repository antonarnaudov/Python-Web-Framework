from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Python(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    image = models.URLField()


class Wishes(models.Model):
    python = models.ForeignKey(Python, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
