donut={"type":"donut","flavors":{"flavor":[{"type":"chocolate","id":"1001"}, {"type":"glazed","id":"1002"},{"type":"sprinkled","id":"1003"}]}}

#Parse JSON without loops
print(donut["flavors"]["flavor"][0]["id"] + "  " + donut["flavors"]["flavor"][0]["type"])
print(donut["flavors"]["flavor"][1]["id"] + "  " + donut["flavors"]["flavor"][1]["type"])
print(donut["flavors"]["flavor"][2]["id"] + "  " + donut["flavors"]["flavor"][2]["type"])
print()

#Parse JSON with loops
for hungry in donut["flavors"]["flavor"]:
	print(hungry["id"] + "  " + hungry["type"])
print()
	

cars={"sports":{"porsche":"Volkswagon","Viper":"Dodge","Corvette":"Chevy"}}
#Parse JSON without loops
print("porsche  " + cars["sports"]["porsche"])
print("Viper  " + cars["sports"]["Viper"])
print("Corvette  " + cars["sports"]["Corvette"])
print()

#Parse JSON with loops
for auto in cars["sports"]:
	print(auto + "  " + cars["sports"][auto])
