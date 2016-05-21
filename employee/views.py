from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext,Context
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotAllowed
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import connection


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

@login_required
def add_employee(request):
    if request.method == 'POST':
        emp_name = request.POST.get('emp_name')
        emp_no = request.POST.get('emp_no')
        cursor = connection.cursor()
        cursor.execute("CALL ins_emps('"+str(emp_name)+"',"+str(emp_no)+");")
        cursor.close()
    return render_to_response('employee.html',  context_instance = RequestContext(request)) 

@login_required
def list_employee(request):
    cursor = connection.cursor()
    cursor.execute("CALL get_all_emps();")
    emp_list = dictfetchall(cursor)
    cursor.close()
    return render_to_response('emp_list.html',  {'emp_list': emp_list}, context_instance = RequestContext(request))

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        imei = request.POST['imei']
        mac = request.POST['mac']
        user = authenticate(imei = imei, mac = mac)
        if user is not None:
            login(request, user)
            logauth = {'success':True, 'msg':'login Success'}
            response = JsonResponse(logauth)
        else:
            logauth = {'success':False, 'msg':'login Failed'}
            response = JsonResponse(logauth)
            response.status_code = 401        
        return response
    return HttpResponseNotAllowed('POST')

