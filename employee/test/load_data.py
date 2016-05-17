from employee.models import Profile 


def profile_data(imei,mac):
	data = Profile.objects.filter(imei=imei) | Profile.objects.filter(mac=mac)
	if not data:
		print "---------DATA SAVED-----------------"
		data = Profile(imei=imei, mac=mac)
		data.save()
	else:
		print "--------USER ALREADY EXISTED----------"

profile_data(1,1)




