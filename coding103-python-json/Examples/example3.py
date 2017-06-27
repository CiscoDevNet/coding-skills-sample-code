import requests
import json


# Request the x-auth-token
url = "https://sandboxapic.cisco.com/api/v1/ticket"
# Request Body
payload = """{
    "username":"devnetuser",
    "password":"Cisco123!"
    }"""

# HTTP Headers
headers = {
    'content-type': "application/json"
    }

# Execute request
response = requests.request("POST", url, data=payload, headers=headers, verify=False)

# Print request
print(response.text)

# Load the response into a JSON object
json_response = json.loads(response.text)

# Parse the service ticket out of the JSON
service_ticket = json_response['response']['serviceTicket']

# Print the service ticket
print(service_ticket)

# Request the x-auth-token
url = "https://sandboxapic.cisco.com/api/v1/host"

# HTTP Headers
headers = {
    'content-type': "application/json",
    'x-auth-token': service_ticket
    }

# Execute request to get hosts, set equal to host_response
host_response = requests.request("GET", url, data=payload, headers=headers, verify=False)

#Print the reponse data
print(host_response.text)

#Load the response into a json object
host_response = json.loads(host_response.text)

# loop through the response, return the host IP and connection type
for i, body in enumerate(host_response["response"]):
    host = body['hostIp']
    connection = body['hostType']
    message = "Host %i's ip is %s and uses a %s connection!\n" % (i + 1, host, connection)
    print(message)