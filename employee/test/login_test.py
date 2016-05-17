import requests

class LoginCheck:
	def __init__(self):
		self.session = requests.Session()
		self.a = 1
	def check_login_success(self,imei,mac):
		url = "http://127.0.0.1:8000/login/"
		data = {"imei":imei, "mac":mac}
		response = self.session.post(url, data=data)
		#print ".............login json response.........."
		#print response.json()
		#print ".............login headers response.........."
		#print response.headers
		#print ".............login response.request.headers.........."
		#print response.request.headers
		print "...LOGIN STATUS CODE....", response.status_code
	def check_employee_success(self):
		url =  "http://127.0.0.1:8000/employee_list/"
		response = self.session.get(url)
		#print ".............employee_list json response.........."
		#print response.json()
		#print ".............employee_list response.headers.........."
		#print response.headers
		#print ".............employee_list response.request.headers.........."
		#print response.request.headers
		print "...EMP STATUS CODE....", response.status_code

print "-------SUCCESS LOGIN-----------"
obj = LoginCheck()
obj.check_login_success(124,986)
obj.check_employee_success()
print "--------FAILED LOGIN-----------"
obj = LoginCheck()
obj.check_login_success(14,86)
obj.check_employee_success()

