from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext,Context
#from django.template.loader import get_template
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
#from django.db.models import F
#from django import forms
#from django.conf import settings
#import time,datetime, string, random
#import ho.pisa
#import StringIO 
#from xhtml2pdf import pisa
#from django.utils.html import escape
#from dateutil.relativedelta import relativedelta
#import json,datetime
#from django.utils.html import escape
#from django.utils.translation import ugettext as _
#from django.core import serializers
#from django.core import serializers
#from adduser.utils import custom_serialize
#from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
import MySQLdb
from django.http import JsonResponse



def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def get_db_conn():
	db = MySQLdb.connect(host="localhost", user="dbadmin", passwd="dbadmin1", db="test", port=3306)
	return db

def employee_form(request):
	if request.method == 'POST':
		emp_name = request.POST.get('emp_name')
		emp_no = request.POST.get('emp_no')
		db = get_db_conn()
		cursor = db.cursor()
		cursor.execute("CALL ins_emps('"+str(emp_name)+"',"+str(emp_no)+");")
		cursor.close()
		db.commit()
		db.close()
	return render_to_response('employee.html',  context_instance = RequestContext(request))	
@login_required
def employee_list(request):
	#import pdb; pdb.set_trace();
	db = get_db_conn()
	cursor = db.cursor()
	cursor.execute("CALL get_all_emps();")
	emp_list = dictfetchall(cursor)
	cursor.close()
	db.commit()
	db.close()
	return render_to_response('emp_list.html',  {'emp_list': emp_list}, context_instance = RequestContext(request))


@csrf_exempt
def login_view(request):
	if request.method == 'POST':
		imei = request.POST['imei']
		mac = request.POST['mac']
		user = authenticate(imei = imei, mac = mac)
		
		if user is not None:
			login(request, user)
			logauth = {'Success':True, 'msg':'login Success'}
		else:
			logauth = {'Success':False, 'msg':'login Failed'}
		return JsonResponse(logauth)


