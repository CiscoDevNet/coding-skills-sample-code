# Example of getting network-devices via REST API calls from Python

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


# import requests library
import requests

#import json library
import json

#controller='sandboxapic.cisco.com'
controller='devnetapi.cisco.com/sandbox/apic_em'

def getTicket():
	# put the ip address or dns of your apic-em controller in this url
	url = "https://" + controller + "/api/v1/ticket"

	#the username and password to access the APIC-EM Controller
	payload = {"username":"devnetuser","password":"Cisco123!"}

	#Content type must be included in the header
	header = {"content-type": "application/json"}

	#Performs a POST on the specified url to get the service ticket
	response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)

	print (response)
	
	#convert response to json format
	r_json=response.json()

	#parse the json to get the service ticket
	ticket = r_json["response"]["serviceTicket"]

	return ticket


def getNetworkDevices(ticket):
	# URL for network-device REST API call to get list of exisiting devices on the network.
	url = "https://" + controller + "/api/v1/network-device"

	#Content type as well as the ticket must be included in the header 
	header = {"content-type": "application/json", "X-Auth-Token":ticket}

	# this statement performs a GET on the specified network device url
	response = requests.get(url, headers=header, verify=False)

	# json.dumps serializes the json into a string and allows us to
	# print the response in a 'pretty' format with indentation etc.
	print ("Network Devices = ")
	print (json.dumps(response.json(), indent=4, separators=(',', ': ')))
	
	#convert data to json format.
	r_json=response.json()
	
	#Iterate through network device data and print the id and series name of each device
	for i in r_json["response"]:
		print(i["id"] + "   " + '{:53}'.format(i["series"]) + "  " + i["reachabilityStatus"])
		


theTicket=getTicket()
getNetworkDevices(theTicket)
