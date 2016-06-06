food={"vegetables":["carrots","kale","cucumber","tomato"]}

cars={"sports":{"Porsche":"Volkswagon","Viper":"Dodge","Corvette":"Chevy"}}


print(food["vegetables"])
print(food["vegetables"][1])

print(cars["sports"])
print(cars["sports"]["Viper"])

my_car=cars["sports"]["Viper"]
print(my_car)


#Assignment
dessert={"iceCream":["Rocky-Road","strawberry","Pistachio-Cashew","Pecan-Praline"]}
d=dessert["iceCream"][1]
print(d)
for yummy in dessert["iceCream"]:
    print(yummy)

soup={"soup":{"tomato":"healthy","onion":"bleh!","vegetable":"goodForYou"}}
s=soup["soup"]["vegetable"]
print(s)
for food in soup["soup"]:
    print(food + " " + soup["soup"][food])


def my_func (net):
    for n1 in net["Network"]["router"]:
        print(n1 + " " + net["Network"]["router"][n1])
        
network={"Network":{"router":{"ipaddress":"192.168.1.21","mac_address":"08:56:27:6f:2b:9c"}}}
n=network["Network"]["router"]["mac_address"]
print(n)
my_func(network)


                       