from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from pythons_app.models import Python


class UserProfile(models.Model):
    date_of_birth = models.DateField(blank=False)
    image = models.ImageField(upload_to='profiles/')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
