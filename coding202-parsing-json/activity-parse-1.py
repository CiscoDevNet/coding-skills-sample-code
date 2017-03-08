from urllib.request import Request, urlopen
import json

req = Request('http://jsonplaceholder.typicode.com/users', headers={'User-Agent': 'Mozilla/5.0'})
# req = Request('http://127.0.0.1:8000/object')
# req = Request('http://127.0.0.1:8000/array')
# req = Request('http://127.0.0.1:8000/random')
# req = Request('http://127.0.0.1:8000/random/array')
# req = Request('http://127.0.0.1:8000/complex')
# req = Request('http://127.0.0.1:8000/complex/array')

response = urlopen(req)
response_string = response.read().decode("utf-8")

json_object = json.loads(response_string)

print(json_object)
#print(json.dumps(json_object, sort_keys=True, indent=4))
#print(json_object[4])
#print(json.dumps(json_object[4], sort_keys=True, indent=4))
#print(json_object[4]["name"])
#print(json_object[4]["address"]["geo"])
#print(json_object[4]["address"]["geo"]["lat"])
#print(json_object[4]["address"]["geo"]["lng"])

response.close()
