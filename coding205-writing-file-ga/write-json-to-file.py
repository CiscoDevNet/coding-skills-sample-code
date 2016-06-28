# Coding 205 Example
# This example retrieves a list of network devices using the APIC-EM APIs
# Then we write the network device ID and type for each device out to a file.


# * THIS SAMPLE APPLICATION AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY
# * OF ANY KIND BY CISCO, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED
# * TO THE IMPLIED WARRANTIES OF MERCHANTABILITY FITNESS FOR A PARTICULAR
# * PURPOSE, NONINFRINGEMENT, SATISFACTORY QUALITY OR ARISING FROM A COURSE OF
# * DEALING, LAW, USAGE, OR TRADE PRACTICE. CISCO TAKES NO RESPONSIBILITY
# * REGARDING ITS USAGE IN AN APPLICATION, AND IT IS PRESENTED ONLY AS AN
# * EXAMPLE. THE SAMPLE CODE HAS NOT BEEN THOROUGHLY TESTED AND IS PROVIDED AS AN
# * EXAMPLE ONLY, THEREFORE CISCO DOES NOT GUARANTEE OR MAKE ANY REPRESENTATIONS
# * REGARDING ITS RELIABILITY, SERVICEABILITY, OR FUNCTION. IN NO EVENT DOES
# * CISCO WARRANT THAT THE SOFTWARE IS ERROR FREE OR THAT CUSTOMER WILL BE ABLE
# * TO OPERATE THE SOFTWARE WITHOUT PROBLEMS OR INTERRUPTIONS. NOR DOES CISCO
# * WARRANT THAT THE SOFTWARE OR ANY EQUIPMENT ON WHICH THE SOFTWARE IS USED WILL
# * BE FREE OF VULNERABILITY TO INTRUSION OR ATTACK. THIS SAMPLE APPLICATION IS
# * NOT SUPPORTED BY CISCO IN ANY MANNER. CISCO DOES NOT ASSUME ANY LIABILITY
# * ARISING FROM THE USE OF THE APPLICATION. FURTHERMORE, IN NO EVENT SHALL CISCO
# * OR ITS SUPPLIERS BE LIABLE FOR ANY INCIDENTAL OR CONSEQUENTIAL DAMAGES, LOST
# * PROFITS, OR LOST DATA, OR ANY OTHER INDIRECT DAMAGES EVEN IF CISCO OR ITS
# * SUPPLIERS HAVE BEEN INFORMED OF THE POSSIBILITY THEREOF.-->

# import the requests library so we can use it to make REST calls (http://docs.python-requests.org/en/latest/index.html)
import requests

# import the json library.  This library gives us many handy features for formatting, displaying
# and manipulating json.
import json

# All of our REST calls will use the url for the APIC EM Controller as the base URL
# So lets define a variable for the controller IP or DNS so we don't have to keep typing it
#controller_url = "https://sandboxapic.cisco.com"
controller_url='https://devnetapi.cisco.com/sandbox/apic_em'


#the username and password to access the APIC-EM Controller
payload = {"username":"devnetuser","password":"Cisco123!"}

ticket_url = controller_url + "/api/v1/ticket"

#Content type must be included in the header
header = {"content-type": "application/json"}

#Performs a POST on the specified url to get the service ticket
response= requests.post(ticket_url,data=json.dumps(payload), headers=header, verify=False)
	
#convert response to json format
r_json=response.json()

#parse the json to get the service ticket
ticket = r_json["response"]["serviceTicket"]

# Get Devices
# This function allows you to view a list of 3 of the devices in the network(routers and switches).
get_devices_url = controller_url + '/api/v1/network-device/1/3'

#Content type as well as the ticket must be included in the header 
header = {"content-type": "application/json", "X-Auth-Token":ticket}
	
#Perform GET on get_devices_url
get_devices_response = requests.get(get_devices_url, headers=header, verify=False)

# The json method of the response object returned by requests.get returns the request body in json format
get_devices_json = get_devices_response.json()

#Now let's read and display some specific information from the json

# set our parent as the top level response object
parent =  get_devices_json["response"]

print ("Devices = ")
# you can open the file using 'with'.
# 'with' gives you better exception handling and when you use 'with' the file automatically be closed
with open("list-of-devices.txt", "w") as file:
    # for each device returned, write the networkDeviceId and type value to the file
    for item in parent:
        device="id = " + item["id"] + " type = " + item["type"]
        file.write (device + "\n")
        print(device)
		 


