from urllib.request import Request, urlopen
import json

uri_cmx = 'https://devnetapi.cisco.com/sandbox/mse/api/config/v1/maps/info/CiscoCampus'


# Let's wrap our common get functionality in a function definition
def get_content(uri):
    req = Request(uri)
    req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc=')
    # req.add_header('Accept', 'application/json')
    response = urlopen(req)
    response_string = response.read().decode("utf-8")
    response.close()
    return response_string


json_object = json.loads(get_content(uri_cmx))

building_names = []

buildings = json_object["buildingList"]
for building in buildings:
    building_names.append(building["name"])

print(building_names)
print(type(building_names))

# for building_name in building_names:
#     building_uri = uri_cmx + "/" + building_name
#     print(building_uri)
#     print(get_content(building_uri))
