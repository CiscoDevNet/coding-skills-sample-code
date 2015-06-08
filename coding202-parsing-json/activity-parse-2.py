from urllib.request import Request, urlopen
import json

req = Request('https://msesandbox.cisco.com/api/contextaware/v1/maps/info/DevNetCampus')
req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc==')
req.add_header('Accept', 'application/json')
response = urlopen(req)
responseString = response.read().decode("utf-8")

jsonObject = json.loads(responseString)

print(jsonObject["Campus"]["Building"])

#buildings = jsonObject["Campus"]["Building"]
#for building in buildings:
#	print(building["name"])

response.close()