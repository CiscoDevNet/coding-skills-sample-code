from urllib.request import Request, urlopen
import json

req = Request('http://jsonplaceholder.typicode.com/users')
response = urlopen(req)
response_string = response.read().decode("utf-8")

json_object = json.loads(response_string)

print(json_object)
#print(json_object[4])
#print(json_object[4]["name"])
#print(json_object[4]["address"]["geo"])
#print(json_object[4]["address"]["geo"]["lat"])
#print(json_object[4]["address"]["geo"]["lng"])

response.close()