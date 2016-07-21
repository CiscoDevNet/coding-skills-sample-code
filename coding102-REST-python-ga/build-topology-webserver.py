# Example of create a topology web server. This include :
# - building a web server via Flask (http://flask.pocoo.org/)
# - render topology graphic via NeXt UI toolkit (https://wiki.opendaylight.org/view/NeXt:Main)
# - get topology data from APIC-EM via REST API calls from Python

# Before start please install flask by `pip install flask`
# Then use python run this script `python build-topology-webserver.py`
# Use Chrome or Safari opne this link `http://127.0.0.1:5000/`


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


def getNetworkDevices(ticket):
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
    # when call '/' index page, render template 'topology.html' and response to request
    return render_template("topology.html")


# define an reset api to get topology data
@app.route("/api/topology")
def topology():
    # get ticket
    theTicket = getTicket()

    # get topology data and return `jsonify` string to request
    return jsonify(getNetworkDevices(theTicket))


if __name__ == "__main__":
    app.run()
