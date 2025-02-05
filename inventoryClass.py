# This file is going to be used for me to practice
# using classes by creating an inventory class 
# that has many instances of different items

class Inventory(object):
	def __init__(self,name = "Default Name",UOM = "Unit of Measure"\
			  ,unitPrice = 0,quantity = 0):
		self.name = name
		self.UOM = UOM
		self.unitPrice = unitPrice
		self.quantity = quantity
	description = ""
	def fullDescription(self):
		print("The there are %i %ss of the %s item each worth $%i" % \
		(self.quantity,self.UOM,self.name,self.unitPrice))

inventoryList = []

couch = Inventory("Love Sofa","unit",599.99,4)
print(couch.UOM)
print(couch.quantity)
print(couch.description)
couch.description = "This couch reclines and is perfect for a \
spacious living room"
print(couch.description)

tub = Inventory("Tub","unit",350,3)
masterTub = Inventory("Partner Jacuzzi","unit",2500,1)
californiaKingBed = Inventory("Califonia King Memory Foam Bed", "unit", 1500,1)

inventoryList.append(couch)
inventoryList.extend([masterTub,tub,californiaKingBed])

for item in inventoryList:
	item.description = input("What is the \
description for %s?: " % item.name)

for item in inventoryList:
	print(item.description)

testInv = Inventory()
print(testInv.name)
californiaKingBed.fullDescription()
testInv.fullDescription()


# Im very happy with today's session
# Learned a lot, quick




# Continuation the next day, February 20

class Food(Inventory):
	def __init__(self, name="Default Food", UOM="Unit of Food", unitPrice=10, quantity=10):
		super().__init__(name, UOM, unitPrice, quantity)
		print("Created food instance")
	foodCategory = ""

apple = Food()
apple.fullDescription()

banana = Food(quantity=15,unitPrice=15)
print(banana.name)
print(banana.quantity)

banana.foodCategory = "fruit"
print(banana.foodCategory)
print(apple.foodCategory)
apple.foodCategory = "fruit"
print(apple.foodCategory)













