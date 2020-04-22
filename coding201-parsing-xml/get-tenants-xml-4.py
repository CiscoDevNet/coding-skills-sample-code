import requests
import xml.dom.minidom
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
# We leverage the .xml ending to receive the data back as XML
tenants = requests.get("https://sandboxapicdc.cisco.com/api/node/class/fvTenant.xml?rsp-subtree-include=health,faults", headers=header, verify=False)

# Now lets use DOM to clean up the XML from its completely raw format
dom = xml.dom.minidom.parseString(tenants.text)
xml = dom.toprettyxml()
print(xml)

# Now we'll do something similar, but done using a direct access method of the data, rather than interation and loops
tenant_list = dom.getElementsByTagName('fvTenant')
for tenants in tenant_list:
    tenant_name = tenants.getAttribute('name')
    tenant_dn = tenants.getAttribute('dn')
    health_score = tenants.firstChild.getAttribute('cur')
    output = "Tenant: " + tenant_name + "\t Health Score: " + health_score + "\n DN: " + tenant_dn
    print(output.expandtabs(40))