# Example of render a topology via a web server. This include :
# - building a web server via Flask (http://flask.pocoo.org/)
# - render topology graphic via NeXt UI toolkit (https://wiki.opendaylight.org/view/NeXt:Main)
# - get topology data from APIC-EM via REST API calls from Python

# Before start please install flask by `pip install flask`
# Then use python run this script via: python build-topology-webserver.py
# Use Chrome or Safari browser. In the url field enter this link: `http://127.0.0.1:5000/`

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

# import json library
import json

# import flask web framewoork
from flask import Flask

# from flask import render_template function
from flask import render_template, jsonify

# controller='sandboxapic.cisco.com'
controller = 'devnetapi.cisco.com/sandbox/apic_em'


def getTicket():
    # put the ip address or dns of your apic-em controller in this url
    url = "https://" + controller + "/api/v1/ticket"

    # the username and password to access the APIC-EM Controller
    payload = {"username": "devnetuser", "password": "Cisco123!"}

    # Content type must be included in the header
    header = {"content-type": "application/json"}

    # Performs a POST on the specified url to get the service ticket
    response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)

    print(response)

    # convert response to json format
    r_json = response.json()

    # parse the json to get the service ticket
    ticket = r_json["response"]["serviceTicket"]

    return ticket


def getTopology(ticket):
    # URL for network-device REST API call to get list of exisiting devices on the network.
    url = "https://" + controller + "/api/v1/topology/physical-topology"

    # Content type as well as the ticket must be included in the header
    header = {"content-type": "application/json", "X-Auth-Token": ticket}

    # this statement performs a GET on the specified network device url
    response = requests.get(url, headers=header, verify=False)

    # convert data to json format.
    r_json = response.json()

    # return json object
    return r_json["response"]


# intialize a web app
app = Flask(__name__)
	
# define index route to return topology.html
@app.route("/")
def index():
    # when called '/' which is the default index page, render the template 'topology.html'
    return render_template("topology.html")


# define an reset api to get topology data
@app.route("/api/topology")
def topology():
    # get ticket
    theTicket = getTicket()

    # get topology data and return `jsonify` string to request
    return jsonify(getTopology(theTicket))

	

if __name__ == "__main__":
    app.run()
