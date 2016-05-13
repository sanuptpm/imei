from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:

	url(r'^$', 'employee.views.employee_form', name='employee_form'),
	url(r'^employee_list/', 'employee.views.employee_list', name='employee_list'),
	url(r'^login/', 'employee.views.login_view', name='login'),
	
	
)
