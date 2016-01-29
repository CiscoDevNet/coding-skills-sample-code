# import requests library
import requests

#import json library
import json

# put the ip address or dns of your apic-em controller in this url
url = 'https://sandboxapic.cisco.com:9443/api/v1/ticket'

#the username and password to access the APIC-EM Controller
payload = {"username":"admin","password":"C!sc0123"}

#Content type must be included in the header
header = {"content-type": "application/json"}

#Performs a POST on the specified url.
response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)

# print the json that is returned
print(response.text)