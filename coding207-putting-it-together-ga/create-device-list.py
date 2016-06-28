# Coding 207 - Putting it all together example
# Asks the user to choose router or switch
# Retrieves list of devices using APIC-EM
# Writes list of devices of selected type to a file


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

#import logging library
import logging

# Disable warnings
requests.packages.urllib3.disable_warnings() 


# All of our REST calls will use the url for the APIC EM Controller as the base URL
#controller_url = "https://sandboxapic.cisco.com"
controller_url='https://devnetapi.cisco.com/sandbox/apic_em'


def getUserInput():
	#turn on logging to the mylog.log file
	logging.basicConfig(filename='mylog.log',format='%(asctime)s %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

	logging.info("Begin")
	logging.info("Asking user for device type")
	
	# Ask the user what kind of list they want to create
	device_type = input("Do you want to create a list of [r]outers or [s]witches?")

	# create a variable called type to hold which kind of device to save
	if device_type == 'r':
		type = "router"
	else:
		type = "switch"

	logging.info("Device type is " + type)

	# Ask user for name of the file
	file_name = input("Specify the file name to use for the list:")

	logging.info("Will save device list to " + file_name)

	return(type,file_name)


#creates and returns a service ticket.
def getTicket():
	logging.info("\nCreating ticket")
	# put the ip address or dns of your apic-em controller in this url
	url = controller_url + "/api/v1/ticket"

	#the username and password to access the APIC-EM Controller
	payload = {"username":"devnetuser","password":"Cisco123!"}

	#Content type must be included in the header
	header = {"content-type": "application/json"}

	#Performs a POST on the specified url to get the service ticket
	response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)

	logging.info(response.text)
	
	#convert response to json format
	r_json=response.json()

	#parse the json to get the service ticket
	ticket = r_json["response"]["serviceTicket"]

	return ticket

	
def getDeviceCount(ticket):
	# Specify URL for the devices count
	devices_count_url = controller_url + '/api/v1/network-device/count'

	logging.info("Calling APIC-EM API url:" + devices_count_url)
	
	#Content type as well as the ticket must be included in the header 
	header = {"content-type": "application/json", "X-Auth-Token":ticket}
	
	# Perform GET on devices_count_url
	devices_count_response = requests.get(devices_count_url, headers=header, verify=False)
	count = devices_count_response.json()["response"]

	logging.debug("API response: " + json.dumps(devices_count_response.json(), indent=4, separators=(',', ': ')))
	
	return count

	
# Get Devices
# This function allows you to view a list of all the devices in the network(routers and switches) with the maximum shown specified by the passed in count variable
def getDevices(ticket,count,type,file_name):
	get_devices_url = controller_url + '/api/v1/network-device/1/' + str(count)

	logging.info("Calling APIC-EM API url:" + get_devices_url)
	
	#Content type as well as the ticket must be included in the header 
	header = {"content-type": "application/json", "X-Auth-Token":ticket}
	
	#Perform GET on get_devices_url
	get_devices_response = requests.get(get_devices_url, headers=header, verify=False)

	# The json method of the response object returned by requests.get returns the request body in json format
	get_devices_json = get_devices_response.json()

	logging.debug("API response: " + json.dumps(get_devices_json, indent=4, separators=(',', ': ')))	

	#Now let's parse the json and write the devices out to our file
	file= open(file_name, "w")
	logging.info("File opened:" + file_name)
	logging.info("Begin writing list:" + file_name)
	file.write ("The list of devices of type: " + type + "\n" )
	
	# set our parent as the top level response object
	parent =  get_devices_json["response"]
    
	# for each device returned, write the networkDeviceId and type value to the file if the type corresponds to what we're seeking.
	for item in parent:
		lowerCaseType=item["type"].lower()
		if lowerCaseType.find(type)!=-1:
			file.write ("id = " + item["id"] + " type = " + item["type"] + "\n")

	print ("Finished writing list ...")
	logging.info("End writing list:" + file_name)


(theType,theFilename)=getUserInput()
theTicket=getTicket()
theCount=getDeviceCount(theTicket)
getDevices(theTicket,theCount,theType,theFilename)
