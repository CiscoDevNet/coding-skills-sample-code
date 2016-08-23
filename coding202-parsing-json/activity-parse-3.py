from urllib.request import Request, urlopen
import json

req = Request('https://devnetapi.cisco.com/sandbox/mse/api/config/v1/maps/info/DevNetCampus/DevNetBuilding')
req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc=')
response = urlopen(req)
response_string = response.read().decode('utf-8')

json_object = json.loads(response_string)

print(json_object['floorList'])

# Parse out the floors from the result set
# floors = json_object["floorList"]
# for floor in floors:
#     print(floor['name'] + ' Floor Number: ' + str(floor['floorNumber']))
#     # Parse out the access points from the returned floors
#     # aps = floor["accessPoints"]
#     # for ap in aps:
#     #     print('\t' + ap['name'] + '/' + ap['radioMacAddress'])

response.close()