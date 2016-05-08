from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:

	url(r'^$', 'employee_view.views.employee_form', name='employee_form'),
	url(r'^employee_list/', 'employee_view.views.employee_list', name='employee_list'),
	url(r'^login/', 'employee_view.views.login_view', name='login'),
	
	
)
