# Getting started with APIC-EM APIs 
# Follows APIC-EM Basics Learning Lab
# Basics Learning Lab Full example for Get Devices, Get Hosts, Get Policies, Get Applications

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

# import the json library.  This library provides handy features for formatting, displaying
# and manipulating json.
import json

# All of our REST calls will use the url for the APIC EM Controller as the base URL
# So lets define a variable for the controller IP or DNS so we don't have to keep typing it
controller_url = "http://sandboxapic.cisco.com/"

# Get Devices
# This function allows you to view a list of all the devices in the network(routers and switches).
get_devices_url = controller_url + 'api/v0/network-device'

#Perform GET on get_devices_url and load response into a json object
get_devices_response = requests.get(get_devices_url)

get_devices_json = get_devices_response.json()


#Now let's read and display some specific information from the json

# set our parent as the top level response object
parent =  get_devices_json["response"]

print ("Devices = ")

# for each device returned, print the networkDeviceId
for item in parent:
         print (item["id"])
      

# Get Hosts
# This function allows you to view a list of all the hosts in the network.
get_hosts_url = controller_url + 'api/v0/host'

#Perform GET on get_hosts_url and load response into a json object
get_hosts_response = requests.get(get_hosts_url)

get_hosts_json = get_hosts_response.json()

#Now let's read and display some specific information from the json

# set our parent as the top level response object
hosts_parent =  get_hosts_json["response"]

print ("Hosts= ")

# for each device returned, print the networkDeviceId
for item in hosts_parent:
         print (item["hostIp"])
         

# Get Policies
# This function allows you to view a list of all the policies in the network.
get_policies_url = controller_url + 'api/v0/policy'

#Perform GET on get_hosts_url and load response into a json object
get_policies_response = requests.get(get_policies_url)

get_policies_json = get_policies_response.json()

#Now let's read and display some specific information from the json

# set our parent as the top level response object
policies_parent =  get_policies_json["response"]

print ("Policies= ")

# for each device returned, print the networkDeviceId
for item in policies_parent:
         print (item["id"])
         
         

# Get Applications
# This function allows you to view a list of all the applications in the network.
get_apps_url = controller_url + 'api/v0/application'

#Perform GET on get_hosts_url and load response into a json object
get_apps_response = requests.get(get_apps_url)

get_apps_json = get_apps_response.json()

#Now let's read and display some specific information from the json

# set our parent as the top level response object
apps_parent =  get_apps_json["response"]

print ("Applications= ")

# for each device returned, print the networkDeviceId
for item in apps_parent:
         print (item["name"])