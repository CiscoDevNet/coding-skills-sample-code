from urllib.request import Request, urlopen
import json

uri = 'https://devnetapi.cisco.com/sandbox/mse/api/config/v1/maps/info/DevNetCampus'


def get_content(uri):
    req = Request(uri)
    req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc=')
    req.add_header('Accept', 'application/json')
    response = urlopen(req)
    response_string = response.read().decode("utf-8")
    response.close()
    return response_string


json_object = json.loads(get_content(uri))

building_names = []

buildings = json_object["buildingList"]
for building in buildings:
    building_names.append(building["name"])

# Print out the building names found - this is a Python list
print(building_names)

# Get the content for each of the buildings found by iterating through the building list
for building_name in building_names:
    building_uri = uri + "/" + building_name
    print(building_uri)
    print(get_content(building_uri))
