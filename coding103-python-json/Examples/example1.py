# Import Statements
import json

#This is our JSON sample
string = """
{
  "first_name": "Jacob",
  "last_name": "Adams"
}

"""

# Print out the JSON sample
print("This is just a string \n " + string)

# Load the data into a JSON object
json_data = json.loads(string)

# Extract first name from the object and assign it to a variable
name = json_data["first_name"]

# Print the extracted data to the terminal, to show us it worked.
print("My first name is: " + name)