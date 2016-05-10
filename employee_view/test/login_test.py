import requests

url = "http://127.0.0.1:8000/login/"

session = requests.Session()

#Login request
data = {"imei":"124", "mac":"986"}



response = session.post(url, data=data)

print ".............login json response.........."

print response.json()

print ".............login headers response.........."

print response.headers

print ".............login response.request.headers.........."

print response.request.headers

login_status = requests.get(url,data=data)

print "...login status_code....", login_status.status_code

#Enployee list request
url =  "http://127.0.0.1:8000/employee_list/"

response = session.get(url)

#print ".............employee_list json response.........."

#print response.json()

print ".............employee_list response.headers.........."

print response.headers

print ".............employee_list response.request.headers.........."

print response.request.headers

emp_status = requests.get(url)

print "...emp status code....", emp_status.status_code

#print "...login.....", emp_status.text