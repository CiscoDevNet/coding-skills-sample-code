network1={"Network":{"routers":[{"ipaddress":"192.168.1.21","mac_address":"08:56:27:6f:2b:9c"},{"ipaddress":"192.168.32.15","mac_address":"3a:24:37:4f:5b:1d"}],"switches":[{"ipaddress":"192.168.32.1","mac_address":"3a:24:37:4f:5b:1d"}]}}

def read_network(network1):
    #get the device type name
    for device in network1["Network"]:
        print("Device is: " + device)
        #get the attributes for each device.  Returns a dictionary for each
        for attrib in network1["Network"][device]:
            print("Device attributes are: " + str(attrib))
            #parse the attributes for each device             
            for val in attrib:                
                print ("Device attribute values are: " + val + " " + attrib[val])
        print() #add extra line for separation


read_network(network1)


#Assignment:
network2={"Network":{"routers":[{"ipaddress":"192.168.1.21","mac_address":"08:56:27:6f:2b:9c"}],"switches":[{"ipaddress":"192.168.32.1","mac_address":"3a:24:37:4f:5b:1d"}],"hosts":[{"ipaddress":"192.168.32.5","mac_address":"3b:25:31:4a:5c:3f"},{"ipaddress":"192.168.32.8","mac_address":"4b:15:32:43:51:3c"}]}}





