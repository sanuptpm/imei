from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.utils.crypto import salted_hmac
# Create your models here.


class Profile(AbstractBaseUser):
   imei = models.CharField(max_length=100)
   mac = models.CharField(max_length=128)
   USERNAME_FIELD = 'imei'
   #def get_session_auth_hash(self):
        #key_salt = "django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash"
        #return salted_hmac(key_salt, self.mac).hexdigest()

