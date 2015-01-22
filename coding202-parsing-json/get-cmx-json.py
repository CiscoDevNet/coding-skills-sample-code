from urllib.request import Request, urlopen
import json
req = Request('http://64.103.26.59:8081/api/v0/topology/physical')
req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc==')
req.add_header('Accept', 'application/json')
response = urlopen(req)
responseString = response.read().decode("utf-8")
#print(responseString)
jsonObject = json.loads(responseString)
print(json.dumps(jsonObject, sort_keys=True, indent=4))
response.close()