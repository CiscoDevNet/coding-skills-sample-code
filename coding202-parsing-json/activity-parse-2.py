from urllib.request import Request, urlopen
import json

req = Request('https://devnetapi.cisco.com/sandbox/mse/api/config/v1/maps')
req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc=')
response = urlopen(req)
response_string = response.read().decode('utf-8')

json_object = json.loads(response_string)

print(json_object['campuses'])

# campuses = json_object['campuses']
# for campus in campuses:
#     print(campus['name'])
#     # for building in campus['buildingList']:
#     #     print('\t' + building['name'])

response.close()
