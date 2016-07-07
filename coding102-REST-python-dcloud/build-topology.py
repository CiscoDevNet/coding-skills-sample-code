# Example of building topology via REST API calls from Python

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

# Disable warnings
requests.packages.urllib3.disable_warnings()

controller='198.18.129.100'


def getTicket():
	# put the ip address or dns of your apic-em controller in this url
	url = "https://" + controller + "/api/v1/ticket"

	#the username and password to access the APIC-EM Controller	
	payload = {"username":"admin","password":"C1sco12345"}

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



def getTopology(ticket):
	# URL for topology REST API call to get list of existing devices on the network, and build topology
	url = "https://" + controller + "/api/v1/topology/physical-topology"

	#Content type as well as the ticket must be included in the header 
	header = {"content-type": "application/json", "X-Auth-Token":ticket}

	# this statement performs a GET on the specified network device url
	response = requests.get(url, headers=header, verify=False)

	# json.dumps serializes the json into a string and allows us to
	# print the response in a 'pretty' format with indentation etc.
	print ("Topology = ")
	print (json.dumps(response.json(), indent=4, separators=(',', ': ')))
	
	#convert data to json format.
	r_json=response.json()
	
	#Iterate through network device data and list the nodes, their interfaces, status and to what they connect	
	for n in r_json["response"]["nodes"]:
		if "platformId" in n:
			print()
			print()
			print('{:30}'.format("Node") + '{:25}'.format("Family") + '{:20}'.format("Label")+ "Management IP")
			print('{:30}'.format(n["platformId"]) + '{:25}'.format(n["family"]) + '{:20}'.format(n["label"]) + n["ip"])		
		found=0    #print header flag
		printed=0  #formatting flag
		for i in r_json["response"]["links"]:
			if "startPortName" in i:
				#check that the source device id for the interface matches the node id.  Means interface originated from this device. 
				if i["source"] == n["id"]:
					if found==0:
						print('{:>20}'.format("Source Interface") + '{:>15}'.format("Target") +'{:>28}'.format("Target Interface") + '{:>15}'.format("Status") )
						found=1
						printed=1					
					for n1 in r_json["response"]["nodes"]:
						#find name of node to which this one connects
						if i["target"] == n1["id"]:
							print("    " + '{:<25}'.format(i["startPortName"]) + '{:<18}'.format(n1["platformId"]) + '{:<25}'.format(i["endPortName"]) + '{:<9}'.format(i["linkStatus"]) )							
							break;
		found=0		
		
		for i in r_json["response"]["links"]:
			if "startPortName" in i:
				#Find interfaces that link to this one which means this node is the target. 
				if i["target"] == n["id"]:
					if found==0:
						if printed==1:
							print()
						print('{:>10}'.format("Source") + '{:>30}'.format("Source Interface") + '{:>25}'.format("Target Interface") + '{:>13}'.format("Status"))
						found=1					
					for n1 in r_json["response"]["nodes"]:
						#find name of node to that connects to this one
						if i["source"] == n1["id"]:							
							print("    " + '{:<20}'.format(n1["platformId"]) + '{:<25}'.format(i["startPortName"]) + '{:<23}'.format(i["endPortName"]) + '{:<8}'.format(i["linkStatus"]))
							break;
		
theTicket=getTicket()
getTopology(theTicket)
