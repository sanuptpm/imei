from .models import Profile

class ProfileAuthBackend(object):
	
	def authenticate(self, imei=None, mac=None):
		try:
			user = Profile.objects.get(imei=imei, mac=mac)
			print ".authenticate...user", user
			return user
		except Profile.DoesNotExist:
			return None

