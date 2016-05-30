from .models import Profile

class ProfileAuthBackend(object):
    
    def authenticate(self, imei=None, mac=None):
        try:
            user = Profile.objects.get(imei=imei, mac=mac)
            return user
        except Profile.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Profile.objects.get(pk=user_id)
        except Profile.DoesNotExist:
            return None

