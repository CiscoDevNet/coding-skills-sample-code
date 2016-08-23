from urllib.request import Request, urlopen
import json

req = Request('https://devnetapi.cisco.com/sandbox/mse/api/config/v1/maps/info/DevNetCampus/DevNetBuilding/DevNetZone')
req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc=')
req.add_header('Accept', 'application/json')
response = urlopen(req)
response_string = response.read().decode("utf-8")
# print(responseString)
json_object = json.loads(response_string)
print(json_object)
print(json.dumps(json_object, sort_keys=True, indent=4))
access_points = json_object['accessPoints']
for ap in access_points:
    print('Access Point: ' + ap['name'] + '\t mac: ' + ap['radioMacAddress'])

response.close()
