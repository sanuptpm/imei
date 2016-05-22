from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',

	url(r'^employee$', 'employee.views.add_employee', name='employee_form'),
	url(r'^employees$', 'employee.views.list_employee', name='employee_list'),
	url(r'^login$', 'employee.views.login_view', name='login'),
	
	
)
