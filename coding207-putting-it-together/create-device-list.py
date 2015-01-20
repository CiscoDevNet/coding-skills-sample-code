# Coding 207 - Putting it all together example
# Asks the user to choose router or switch
# Retrieves list of devices using APIC-EM
# Writes list of devices of selected type to a file

# amwhaley@cisco.com
# twitter: @mandywhaley
# http://developer.cisco.com
# http://learninglabs.cisco.com
# Jan 15, 2015

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

import requests
import json

import logging
logging.basicConfig(filename='mylog.log',format='%(asctime)s %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

logging.info("Begin")
logging.info("Asking user for device type")
# Ask the user what kind of list they want to create
device_type = input("Do you want to create a list of [r]outers or [s]witches?")

# create a variable called type to hold which kind of device to save
if device_type == 'r':
        type = "ROUTER"
else:
        type = "SWITCH"

logging.info("Device type is " + type)

# Ask user for name of the file
file_name = input("Specify the file name to use for the list:")

logging.info("Will save device list to " + file_name)

# Get Count of Devices
# All of our REST calls will use the url for the APIC EM Controller as the base URL
# So lets define a variable for the controller IP or DNS so we don't have to keep typing it
controller_url = "https://sandboxapic.cisco.com"

# Specify URL for the devices count
devices_count_url = controller_url + '/api/v0/network-device/count'

logging.info("Calling APIC-EM API url:" + devices_count_url)

# Perform GET on devices_count_url
devices_count_response = requests.get(devices_count_url, verify=False)
count = devices_count_response.json()["response"]

logging.debug("API response: " + json.dumps(devices_count_response.json(), indent=4, separators=(',', ': ')))

# Get Devices
# This function allows you to view a list of all the devices in the network(routers and switches).
# We will specify that the list should start with the first device (1) and end with the last device which is the count of all the devices
# we retrieved in the previous step
get_devices_url = controller_url + '/api/v0/network-device/1/' + str(count)

logging.info("Calling APIC-EM API url:" + get_devices_url)
#Perform GET on get_devices_url
get_devices_response = requests.get(get_devices_url, verify=False)

# The json method of the response object returned by requests.get returns the request body in json format
get_devices_json = get_devices_response.json()

logging.debug("API response: " + json.dumps(get_devices_response.json(), indent=4, separators=(',', ': ')))

#Now let's parse the json and write the devices out to our file

# set our parent as the top level response object
parent =  get_devices_json["response"]


# you can open the file using 'with'.
# 'with' gives you better exception handling and when you use 'with' the file automatically be closed
with open(file_name, "w") as file:
    logging.info("File opened:" + file_name)
    logging.info("Begin writing list:" + file_name)
    file.write ("The list of devices of type: " + type + "\n" )
    # for each device returned, write the networkDeviceId and type value to the file
    for item in parent:
         if item["type"] == type:
             file.write ("id = " + item["id"] + " type = " + item["type"] + "\n")

    print ("Finished writing list ...")
    logging.info("End writing list:" + file_name)

logging.info("End Program")