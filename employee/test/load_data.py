from employee.models import Profile 
from django.db.models import Q

def profile_data(imei,mac):
	data = Profile.objects.filter(Q(imei=imei) | Q(mac=mac))
	if not data:
		print "---------DATA  %d %s SAVED-----------------" %(imei, mac)
		data = Profile(imei=imei, mac=mac)
		data.save()
	else:
		print "--------USER %d %d ALREADY EXISTED----------" %(imei, mac)

# DATA FOR PROFILE
data = [(1,2),(2,2),(3,3)]

for x in data:
	print ""
	profile_data(x[0], x[1])






