from urllib.request import Request, urlopen
import xml.dom.minidom 
req = Request('https://msesandbox.cisco.com/api/contextaware/v1/maps/info/DevNetCampus/DevNetBuilding/DevNetZone')
req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc==')
response = urlopen(req)
responseString = response.read().decode("utf-8")
dom = xml.dom.minidom.parseString(responseString)
xml = dom.toprettyxml()
print(xml)
floor_element = dom.firstChild
if floor_element.hasChildNodes :
 child = floor_element.firstChild
 while child is not None:
     if child.tagName == 'AccessPoint' :
         output = child.tagName + ": " + child.getAttribute('name') + '\t eth: ' + child.getAttribute('ethMacAddress')
         print(output)
     child = child.nextSibling
response.close()