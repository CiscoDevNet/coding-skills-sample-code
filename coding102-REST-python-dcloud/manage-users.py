# Example of calling REST API from Python to manage APIC-EM users/roles using APIC-EM APIs.

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


#creates and returns a service ticket.
def getTicket():
	print("\nCreating ticket")
	# put the ip address or dns of your apic-em controller in this url
	url = "https://" + controller + "/api/v1/ticket"

	#the username and password to access the APIC-EM Controller
	payload = {"username":"admin","password":"C1sco12345"}

	#Content type must be included in the header
	header = {"content-type": "application/json"}

	#Performs a POST on the specified url to get the service ticket
	response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)

	print(response.text)
	
	#convert response to json format
	r_json=response.json()

	#parse the json to get the service ticket
	ticket = r_json["response"]["serviceTicket"]

	return ticket
	
#Get and display the APIC-EM Users
def getUsers(ticket):
	print("\nGetting list of existing users")
	# URL for user REST API call to get list of APIC-EM users.
	url = "https://" + controller + "/api/v1/user"

	#Content type as well as the ticket must be included in the header 
	header = {"content-type": "application/json", "X-Auth-Token":ticket}

	# this statement performs a GET on the specified host url
	response = requests.get(url, headers=header, verify=False)

	# json.dumps serializes the json into a string and allows us to
	# print the response in a 'pretty' format with indentation etc.
	print ("Users = ")
	print (json.dumps(response.json(), indent=4, separators=(',', ': ')))

	
#Adds a APIC-EM User
def addUser(ticket):
	print("\nAdding new user")
	# URL for user REST API call to get list of existing users in the network.
	url = "https://" + controller + "/api/v1/user"

	#Content type as well as the ticket must be included in the header 
	header = {"content-type": "application/json", "X-Auth-Token":ticket}
	
	username="brett"
	#Data for new user
	payload={"password":"Brett123!","username":username,"authorization":[{"scope":"ALL","role":"ROLE_OBSERVER"}]}
	
	# this statement performs a Post on the specified user url
	response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
	print ("Response after post:  " + response.text)
	
	return (username)


#Delete the user that corresponds to the passed in username parameter
def deleteUser(username, ticket):
	print("\nRemoving user: " + username)
	# URL for a specified user REST API call.
	url = "https://" + controller + "/api/v1/user/" + username

	#Content type as well as the ticket must be included in the header 
	header = {"content-type": "application/json", "X-Auth-Token":ticket}

	# this statement performs a Delete on the specified user url
	response = requests.delete(url, headers=header, verify=False)
	print (response.text)

	
#Show the User that corresponds to the passed in username parameter
def showUser(username, ticket):
	print("\nDisplaying user: " + username)
	# URL for user REST API call to get APIC-EM user with corresponding name.
	url = "https://" + controller + "/api/v1/user/" + username

	#Content type as well as the ticket must be included in the header 
	header = {"content-type": "application/json", "X-Auth-Token":ticket}

	# this statement performs a GET on the specified user url
	response = requests.get(url, headers=header, verify=False)
	
	# json.dumps serializes the json into a string and allows us to
	# print the response in a 'pretty' format with indentation etc.
	print ("User found = ")
	print (json.dumps(response.json(), indent=4, separators=(',', ': ')))
	


theTicket=getTicket()
getUsers(theTicket)
name=addUser(theTicket)
showUser(name,theTicket)
getUsers(theTicket)
deleteUser(name,theTicket)
getUsers(theTicket)