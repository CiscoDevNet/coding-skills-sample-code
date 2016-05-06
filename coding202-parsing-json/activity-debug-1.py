from urllib.request import Request, urlopen
import json

uri = 'https://msesandbox.cisco.com/api/contextaware/v1/maps/info/DevNetCampus'

def get_content(uri):
	req = Request(uri)
	req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc==')
	req.add_header('Accept', 'application/json')
	response = urlopen(req)
	responseString = response.read().decode("utf-8")
	response.close()
	return responseString

jsonObject = json.loads(get_content(uri))

building_names = []

buildings = jsonObject["Campus"]["Building"]
for building in buildings:	
	building_names.append(building["name"])

print(building_names)
for building_name in building_names:	
	building_uri = uri + "/" + building_name
	print(building_uri)
	print(get_content(building_uri))
