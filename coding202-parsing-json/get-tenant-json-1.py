import requests
# We need to import the JSON library just to handle our request to the APIC for login
import json


# We need to log in to the APIC and gather a token, before we can access any data
# Let's construct a request with a body

# We'll need to disable certificate warnings
requests.packages.urllib3.disable_warnings()

# We need to have a body of data consisting of a username and password to gather a cookie from APIC
encoded_body = json.dumps({
	        "aaaUser": {
		        "attributes": {
			        "name": "admin",
			        "pwd": "ciscopsdt"
                 }
            }
})

# Now lets make the request and store the data
resp = requests.post("https://sandboxapicdc.cisco.com/api/aaaLogin.json", data=encoded_body, verify=False)

# This stores the received APIC-cookie from the login as a value to be used in subsequent REST calls
header = {"Cookie": "APIC-cookie=" +  resp.cookies["APIC-cookie"]}

# Now we make a call towards the tenant class on the ACI fabric with the proper header value set.
# We leverage the .xml ending to receive the data back as XML.  We're adding health and faults to the printout to ensure that we get levels of data back from the APIC
tenants = requests.get("https://sandboxapicdc.cisco.com/api/node/class/fvTenant.json?rsp-subtree-include=health,faults", headers=header, verify=False)

# Requests stores the text of the response in the .text attribute.  Lets print it to see raw JSON
print(tenants.text)