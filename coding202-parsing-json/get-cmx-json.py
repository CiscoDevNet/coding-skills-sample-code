from urllib.request import Request, urlopen
import json

req = Request('https://devnetapi.cisco.com/sandbox/mse/api/config/v1/maps')
req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc=')
req.add_header('Accept', 'application/json')

response = urlopen(req)
responseString = response.read().decode("utf-8")

jsonObject = json.loads(responseString)

print(json.dumps(jsonObject, sort_keys=True, indent=4))

response.close()
