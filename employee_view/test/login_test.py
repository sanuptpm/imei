import requests

url = "http://127.0.0.1:8000/login/"

session = requests.Session()

#Login request
data = {"imei":"124", "mac":"986"}
response = session.post(url, data=data)

print response.json()

print response.headers

print response.request.headers

#Enployee list request
#url =  "http://127.0.0.1:8000/employee_list/"
#response = session.get(url)

#print response.json()

#print response.headers

#print response.request.headers