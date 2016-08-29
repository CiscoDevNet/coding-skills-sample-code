from urllib.request import Request, urlopen
import xml.dom.minidom 
req = Request('https://msesandbox.cisco.com/api/contextaware/v1/maps/info/DevNetCampus/DevNetBuilding/DevNetZone')
req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc==')
response = urlopen(req)
responseString = response.read().decode("utf-8")
dom = xml.dom.minidom.parseString(responseString)
xml = dom.toprettyxml()
print(xml)
access_points = dom.getElementsByTagName('AccessPoint')
for access_point in access_points:
 ap_name = access_point.getAttribute('name')
 ap_eth_addr = access_point.getAttribute('ethMacAddress')
 ap_ip_addr = access_point.getAttribute('ipAddress')
 print(access_point.tagName + ": " + ap_name + '\t eth: ' + ap_eth_addr + '\t ip: ' + ap_ip_addr)
response.close()