from django.db import models

from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class Profile(AbstractBaseUser):
   imei = models.CharField(max_length=100)
   mac = models.CharField(max_length=128)
   USERNAME_FIELD = 'imei'

