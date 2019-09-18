Before you begin

These code samples are intended to be used with the Cisco DevNet Learning Labs. The Learning Labs will
walk you through the code step by step.

You can find the learning labs here:
https://developer.cisco.com/learning/lab/coding-101-rest-basics-ga/step/1
https://developer.cisco.com/learning/lab/coding-102-rest-python-ga/step/1

You will need to download and setup a few items before you can begin coding along with us.

    Download the Coding 101 sample code and slides
    Your favorite text editor (text wrangler, notepad ++, sublime text etc.)
    Postman Rest Client for Chrome
    Python
        Python is normally pre-installed on Mac OS and most Linux distributions.
        You can also install Python on Windows.
        First, check see if you have Python installed on your system.
        Go to your command prompt and type “python”.
        If you get an error, follow the installations to install python for your system type from this page - http://learnpythonthehardway.org/book/ex0.html
    You will also need to install the Requests Library for Python.
        This is a library that makes it very easy to call REST APIs.
        Follow the instructions to install it here - http://docs.python-requests.org/en/latest/user/install/#install


This download contains the following python examples:

* create-ticket.py – First REST call to create a service ticket which is later used for authentication and role management
* get-network-hosts.py – First application to parse the service ticket response and show list of hosts by doing a pretty print of the JSON data
* get-network-devices.py – Retrieves network device list and parses JSON to display networkDeviceId values
* manage-users.py – Shows how to manage controller access by retrieving, adding and deleting users
