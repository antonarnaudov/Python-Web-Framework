from django.contrib import admin

# Register your models here.
from pythons_auth.models import UserProfile

admin.site.register(UserProfile)
