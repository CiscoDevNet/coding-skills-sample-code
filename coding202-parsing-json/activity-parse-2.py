from urllib.request import Request, urlopen
import json

req = Request('https://msesandbox.cisco.com/api/contextaware/v1/maps/info/DevNetCampus')
req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc==')
req.add_header('Accept', 'application/json')
response = urlopen(req)
response_string = response.read().decode("utf-8")

json_object = json.loads(response_string)

print(json_object["Campus"]["Building"])

#buildings = json_object["Campus"]["Building"]
#for building in buildings:
#	print(building["name"])

response.close()