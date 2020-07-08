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

# Requests stores the text of the response in the .text attribute.  Lets print it to see raw XML
#print(tenants.text)

# Lets make this response a bit prettier, by converting it to a JSON object and using the dumps method to provide indentation
json_response = json.loads(tenants.text)
#print(json.dumps(json_response, sort_keys=True, indent=4))


# We've commented out the pretty-print, but now lets return only the values we want.
# Everything within the returned JSON is containted within the `imdata` dictionary, so lets strip that away
json_tenants = json_response['imdata']

# Now we have to loop through the resulting list (using the `for` loop) and drill into the subsequent dictionaries by name
# When we get to `tenant health`, we move from `attributes` dictionary to `children` dictionary.
# Inside of the `children` dictionary is a list, which will need an index value to move further.
# Since there is only one child object within the `children` list, we can safely set this value to `0`
# This is the result of how the original query was structured, so don't assume you can always set that value to `0`
for tenant in json_tenants:
    tenant_name = tenant['fvTenant']['attributes']['name']
    tenant_dn = tenant['fvTenant']['attributes']['dn']
    tenant_health = tenant['fvTenant']['children'][0]['healthInst']['attributes']['cur']
    output = "Tenant: " + tenant_name + "\t Health Score: " + tenant_health + "\n DN: " + tenant_dn
    print(output.expandtabs(40))