import requests

BASE_URL="http://127.0.0.1:8000/"

class LoginCheck:
    def __init__(self):
        self.session = requests.Session()
    def check_login(self,imei,mac):
        url = BASE_URL+"login"
        data = {"imei":imei, "mac":mac}
        response = self.session.post(url, data=data)
        #print ".............login json response.........."
        #print response.json()
        #print "...............content of the server's response..............."
        #print response.text
        #print ".............login headers response.........."
        #print response.headers
        #print ".............login response.request.headers.........."
        #print response.request.headers
        print "...LOGIN STATUS CODE....", response.status_code
    def check_employee_list(self):
        url =  BASE_URL+"employees"
        response = self.session.get(url)
        #print ".............employee_list json response.........."
        #print response.json()
        #print "...............content of the server's response..............."
        #print response.text
        #print ".............employee_list response.headers.........."
        #print response.headers
        #print ".............employee_list response.request.headers.........."
        #print response.request.headers
        print "...EMP STATUS CODE....", response.status_code
    def check_logout(self):
        url = BASE_URL+"logout"
        response = self.session.get(url)
        print "...LOGOUT STATUS CODE....", response.status_code


print "-------CHECKING SUCCESS LOGIN-----------"
obj = LoginCheck()
obj.check_login(124,986)
obj.check_employee_list()
obj.check_logout()
obj.check_employee_list()

print "--------CHECKING FAILED LOGIN-----------"
obj = LoginCheck()
obj.check_login(14,86)
obj.check_employee_list()