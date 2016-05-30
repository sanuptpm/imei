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
data = [(1,2),(2,2),('352159066842202','c4:50:06:06:c1:d3')]

for x in data:
    print ""
    profile_data(x[0], x[1])






