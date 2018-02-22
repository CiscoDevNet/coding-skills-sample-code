#!/usr/bin/env python3.5

# import requests library
import requests

#import json library
import json

# put the ip address or dns of your apic-em controller in this url
#url = 'https://sandboxapic.cisco.com/api/v1/ticket'
url='https://devnetapi.cisco.com/sandbox/apic_em/api/v1/ticket'



#the username and password to access the APIC-EM Controller
payload = {"username":"devnetuser","password":"Cisco123!"}


#Content type must be included in the header
header = {"content-type": "application/json"}

#Performs a POST on the specified url.
response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)

# print the json that is returned
print(response.text)
