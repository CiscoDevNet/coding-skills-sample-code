# Getting started with APIC-EM APIs
# Follows APIC-EM Basics Learning Lab
# Create a Policy Use Case
# Basic Steps
#	1. Get Hosts
#	2. Get Policies
#	3. Create Policy
#   4. Get Policies again to show new one that was added

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

# import the json library.  This library provides many handy features for formatting, displaying
# and manipulating json.
import json

# All of our REST calls will use the url for the APIC EM Controller as the base URL
# So lets define a variable for the controller IP or DNS so we don't have to keep typing it
controller_url = "https://sandboxapic.cisco.com/"


# Get Hosts
# This function allows you to view a list of all the hosts in the network.
get_hosts_url = controller_url + 'api/v0/host/1/3'

# Perform GET on get_hosts_url
r = (requests.get(get_hosts_url, verify=False))

hosts_obj = r.json()

# For this example, we will use the IP Address of the second host in the list
hosts_parent =  hosts_obj["response"]
selected_host = hosts_parent[2]["hostIp"]

# Print the IP address of this host so we can see it.
print ("\nThis is the selected host = " +  selected_host)

# Get the count of the policies
# Specify URL for policies count
policies_count_url = controller_url + 'api/v0/policy/count'

# Perform GET on policies_count_url
policies_count_response = requests.get(policies_count_url, verify=False)
count = policies_count_response.json()["response"]

# print total number of policies before we create the new one
print ("Total number of policies before = " + str(count))


# get the list of policies
# Specify URL for the list of policies
policies_url = controller_url + 'api/v0/policy/1/' + str(count)

policies_response = requests.get(policies_url, verify=False)

# set our parent as the top level response object
policies_parent =  policies_response.json()

print ("\nPolicies= ")

# Print list of policies before we add the new one
# for each policy returned, print the policyID
for item in policies_parent["response"]:
         print (item["id"])
