# Coding 101
#
#
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

# All of our REST calls will use the url for the APIC EM Controller as the base URL
# So lets define a variable for the controller IP or DNS so we don't have to keep typing it
controller_url = "https://sandboxapic.cisco.com"

# specify url to delete a policy
# Insert the id for the policy that you created into the URL
delete_policy_url = controller_url + '/api/v0/policy/12100233-7c71-4602-ab74-20b87c24fa03'

# Use requests.post to do a DELETE to the policy API
policy_delete_response = requests.delete(delete_policy_url, verify=False)

print ("\nResult of Delete" +  policy_delete_response.text)

###################### Let's check on the status of of the Delete Policy operation. ####################################
# We use the task url that is returned in the response to the Delete to check the status.
task_url = controller_url + policy_delete_response.json()['response']['url']

task_response = requests.get(task_url, verify=False)

print ("Task Progress = " + task_response.json()["response"]["progress"])