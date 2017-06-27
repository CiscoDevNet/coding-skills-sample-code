# Import Statements
import json

# Sample json as a string
string = """
{
	"prop_1001": {
		"type": "apartment",
		"residents": [{
				"resident": "Jacob",
				"phone": "555-1234"
			},
			{
				"resident": "Emily",
				"phone": "555-1235"
			}
		]
	},

	"prop_1002": {
		"type": "condo",
		"residents": [{
				"resident": "Jock",
				"phone": "555-1236"
			},
			{
				"resident": "Kelley",
				"phone": "555-1237"
			}
		]
	}
}

"""

json_string = json.loads(string)

# print out type for 1001
rental_type = str(json_string['prop_1001']['type'])

print("the rental type is: " + rental_type)

# print out the residents on prop_1002
#count = 0
#for i in json_string['prop_1002']["residents"]:
#    print("Resident number %s is %s!" % (str(count), str(i["resident"])))
#    count += 1
"""
for i, data in enumerate(json_string['prop_1002']["residents"]):
    print("Resident number %s is %s!" % (str(i), str(data["resident"])))
"""

