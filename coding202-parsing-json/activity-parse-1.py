from urllib.request import Request, urlopen
import json

req = Request('http://jsonplaceholder.typicode.com/users')
response = urlopen(req)
responseString = response.read().decode("utf-8")

jsonObject = json.loads(responseString)

print(jsonObject)
#print(jsonObject[4])
#print(jsonObject[4]["name"])
#print(jsonObject[4]["address"]["geo"])
#print(jsonObject[4]["address"]["geo"]["lat"])
#print(jsonObject[4]["address"]["geo"]["lng"])

response.close()