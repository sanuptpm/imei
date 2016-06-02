from employee.models import Profile 
from django.db.models import Q

def profile_data(imei,mac):
    data = Profile.objects.filter(Q(imei=imei) | Q(mac=mac))
    if not data:
        print "---------DATA  %s %s SAVED-----------------" %(imei, mac)
        data = Profile(imei=imei, mac=mac)
        data.save()
    else:
        print "--------USER %s %s ALREADY EXISTED----------" %(imei, mac)

# DATA FOR PROFILE
data = [('353043059350234','1c:b0:94:d4:fc:47'),('353327061453619','f8:cf:c5:94:de:ea'),('352159066842202','c4:50:06:06:c1:d3')]

for x in data:
    print ""
    profile_data(x[0], x[1])






