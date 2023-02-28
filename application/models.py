from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser 

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_image')

class AppModel(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='app_image')

