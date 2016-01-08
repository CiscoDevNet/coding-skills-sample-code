# Example of calling REST API from Python to manage network applications using APIC-EM APIs.

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

#import uuid library
import uuid

#import time library
import time

# Disable warnings
requests.packages.urllib3.disable_warnings() 


#controller='sandboxapic.cisco.com:9443'
controller='10.194.104.49'

#creates and returns a service ticket.
def getTicket():
	# put the ip address or dns of your apic-em controller in this url
	url = "https://" + controller + "/api/v1/ticket"

	#the username and password to access the APIC-EM Controller
	#payload = {"username":"admin","password":"1vtG@lw@y"}
	payload = {"username":"admin","password":"devnet123!"}

	#Content type must be included in the header
	header = {"content-type": "application/json"}

	#Performs a POST on the specified url to get the service ticket
	response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)

	#convert response to json format
	r_json=response.json()

	#parse the json to get the service ticket
	ticket = r_json["response"]["serviceTicket"]

	return ticket
	
#Get and display the Network applications
def getNetworkApps(ticket):
	# URL for application REST API call to get list of existing applications in the network.
	url = "https://" + controller + "/api/v1/application"

	#Content type as well as the ticket must be included in the header 
	header = {"content-type": "application/json", "X-Auth-Token":ticket}

	# this statement performs a GET on the specified host url
	response = requests.get(url, headers=header, verify=False)

	# json.dumps serializes the json into a string and allows us to
	# print the response in a 'pretty' format with indentation etc.
	#print ("Applications = ")
	#print (json.dumps(response.json(), indent=4, separators=(',', ': ')))

	#convert data to json format.
	r_json=response.json()

	#Iterate through network device data and print the id and series name of each device
	for i in r_json["response"]:
		if 'popularity' in i:
			if str(i["popularity"])=="1":
				print(str(i["popularity"]) + "   " + i["name"] + "   " + i["category"])


#Adds a network application
def addNetworkApp(ticket):
	# URL for application REST API call to get list of existing applications in the network.
	url = "https://" + controller + "/api/v1/application"

	#Content type as well as the ticket must be included in the header 
	#DON'T KNOW KEY FOR EXPECTED USERNAME. GUESSING HERE.
	header = {"content-type": "application/json", "X-Auth-Token":ticket, "request-username":"admin"}
	
	#create unique id for the application
	id=str(uuid.uuid4())
	
	#create unique id for the category
	categoryID=str(uuid.uuid4())
	
	#Data for new application
	
	#First try - failed with invalid application
	#payload=[{"id":id,"pfrThresholdLossRate":"10","pfrThresholdOneWayDelay":"2", "pfrThresholdJitter":"5", "trafficClass":"BULK_DATA","category":"other","subCategory":"other", "categoryId":categoryID, "popularity":1, "longDescription":"my new cool app","name":"myCoolApp"}]
	
	#Second try - failed with invalid application:  Added new fields starting with ipPort from swagger task investigatoin.
	#payload=[{"id":id,"pfrThresholdLossRate":50,"pfrThresholdOneWayDelay":2,"pfrThresholdJitter":5,"trafficClass":"BULK_DATA","subCategory":"other","categoryId": "9ead1c51-9439-4948-b83b-d127ce4cb3d0","longDescription":"my new cool app","name":"myCoolApp","ipPort":"27333","url":"www.bs.com","dscp":"8","appProtocol":"tcp", "pfrThresholdLossRatePriority": 2, "pfrThresholdOneWayDelayPriority": 1, "pfrThresholdJitterPriority": 3}]
	
#	{
#    "subCategory": "network-management","engineId": "3",popularity": 7,"references": "http://tools.ietf.org/html/rfc3315","name": "dhcpv6-client",
#    "applicationGroup": "other", "tunnel": "false","enabled": "true","tcpPorts": "546","globalId": "L4:546","id": "126e8ab9-4591-4c3b-9ad0-1f0fb9400d21",
#    "indicativeUdpPorts": "546",
#    "longDescription": "DHCPv6 yada yada", "encrypted": "false","pfrThresholdJitter": 1, "udpPorts": "546", "pfrThresholdOneWayDelay": 100,
#   "indicativeTcpPorts": "546","pfrThresholdLossRatePriority": 2,"p2pTechnology": "false","categoryId": "9ead1c51-9439-4948-b83b-d127ce4cb3d0",
#    "pfrThresholdLossRate": 5, "pfrThresholdOneWayDelayPriority": 1, "trafficClass": "OPS_ADMIN_MGMT", "selectorId": "546",
#    "instanceUuid": "126e8ab9-4591-4c3b-9ad0-1f0fb9400d21", "category": "net-admin", "helpString": "DHCPv6 Client","pfrThresholdJitterPriority": 3,
#    "appProtocol": "tcp/udp", "nbarId": "464"}

	#Third try using an existing application - failed with invalid application - Added new fields starting with ipPort from swagger task investigatoin.
	payload=[{"subCategory": "network-management","engineId": "3","popularity": 7,"references": "http://tools.ietf.org/html/rfc3315","name": "dhcpv6-client2","applicationGroup": "other", "tunnel": "false","enabled": "true","tcpPorts": "546","globalId": "L4:546","id": "126e8ab9-4591-4c3b-9ad0-1f0fb9400d21","indicativeUdpPorts": "546", "longDescription": "DHCPv6 yada yada", "encrypted": "false","pfrThresholdJitter": 1, "udpPorts": "546", "pfrThresholdOneWayDelay": 100, "indicativeTcpPorts": "546","pfrThresholdLossRatePriority": 2,"p2pTechnology":"false","categoryId":"9ead1c51-9439-4948-b83b-d127ce4cb3d0","pfrThresholdLossRate": 5, "pfrThresholdOneWayDelayPriority": 1, "trafficClass": "OPS_ADMIN_MGMT","selectorId": "546","instanceUuid": "126e8ab9-4591-4c3b-9ad0-1f0fb9400d21", "category": "net-admin", "helpString": "DHCPv6 Client","pfrThresholdJitterPriority": 3,"appProtocol": "tcp/udp", "nbarId": "464","ipPort":"27333","url":"www.bs.com","dscp":"8","appProtocol":"tcp"}]
	
	# this statement performs a Post on the specified application url
	response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
	print ("Response after post:  " + response.text)
	
	taskURL=response.json()["response"]["url"]
	url = "https://" + controller + taskURL + "/tree"
	response=requests.get(url, headers=header, verify=False)
	print ("Task response:" + response.text)
	
	return (id)


#Delete the network application that corresponds to the passed in appID parameter
def deleteNetworkApp(appID, ticket):
	# URL for application REST API call to get list of existing applications in the network.
	url = "https://" + controller + "/api/v1/application/" + appID

	#Content type as well as the ticket must be included in the header 
	header = {"content-type": "application/json", "X-Auth-Token":ticket}

	# this statement performs a Delete on the specified applicatoin url
	response = requests.delete(url, headers=header, verify=False)
	print (response.text)

	
#Show the network application that corresponds to the passed in appID parameter
def showNetworkApp(appID, ticket):
	# URL for application REST API call to get list of existing applications in the network.
	url = "https://" + controller + "/api/v1/application/" + appID

	#Content type as well as the ticket must be included in the header 
	header = {"content-type": "application/json", "X-Auth-Token":ticket}

	# this statement performs a GET on the specified application url
	response = requests.get(url, headers=header, verify=False)
	if response != None:
		# json.dumps serializes the json into a string and allows us to
		# print the response in a 'pretty' format with indentation etc.
		print ("Application = ")
		print (json.dumps(response.json(), indent=4, separators=(',', ': ')))
	else:
		print ("No applications found with ID: " + appID)



theTicket=getTicket()
getNetworkApps(theTicket)
networkAppID=addNetworkApp(theTicket)
#Hack to wait for app information to be written to the Database.  We'll show a better way to handle this in APIC-EM in lab 207
time.sleep(2)

showNetworkApp(networkAppID,theTicket)
deleteNetworkApp(networkAppID,theTicket)
#Hack to wait for app information to be removed from the Database.  We'll show a better way to handle this in APIC-EM in lab 207
time.sleep(2)
showNetworkApp(networkAppID,theTicket)

