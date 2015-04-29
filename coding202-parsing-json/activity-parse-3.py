from urllib.request import Request, urlopen
import json

req = Request('https://64.103.26.61/api/contextaware/v1/maps/info/DevNetCampus/DevNetBuilding')
req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc==')
req.add_header('Accept', 'application/json')
response = urlopen(req)
responseString = response.read().decode("utf-8")

jsonObject = json.loads(responseString)

print(jsonObject["Building"])

#floors = jsonObject["Building"]["Floor"]
#for floor in floors:
#	print("Floor Number: " + str(floor["floorNumber"]))
#	aps = floor["AccessPoint"]
#	for ap in aps:
#		print(" " + ap["name"] + "/" + ap["ipAddress"] + "/")

response.close()