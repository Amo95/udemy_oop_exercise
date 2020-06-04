"""
LOGIC
write an ecommerce code with python oop
	Requirements:

	Customer details (customer info)
		- customer info

		- add products (name of pruduct and price)
			- keep track of purchases [inventory and product]
				- decrease inventory
		- print purchases

	Products
		- product info
			- product name
			- price/amount

	Inventory (keep track of products and qty in database)
		- add product [add product if product 
			in not in inventory else  increase number to value]
		- print inventory [print from a dict]
"""


class Customer:
	"""Customer info"""
	def __init__(self, name, email):
		self.name = name
		self.email = email
		# store purchases here [item purchased]
		self.purchases = list()

	def add_product(self, inventory, product): # add product to list
		self.inventory = inventory.inventory # assign inventory dict obj [line 56 and 83] to class variable
		if product in self.inventory:
			if self.inventory[product] > 0: # add product to purchases if product is not empty in inventory object
				self.purchases.append(product)
				self.inventory[product] -= 1 # and decrease inventry value by 1
			else:
				print("We are out of stock")
		else:
			print("We don't have this item")

	def print_purchases(self):
		print("Items purchased are:")
		for i in self.purchases: # print items stored in purchases
			print(i.name)	# return and print item/name object in list
		print() # empty line


class Product:
	"""Product info"""
	def __init__(self, name, price): # store product info by defining class variables
	 	self.name = name
	 	self.price = price


class Inventory:
	"""Inventory system"""
	def __init__(self):
		self.inventory = dict() # create a dict-class object

	def add_inventory(self, product, qty):
		if product in self.inventory: #	if value of product already exists, increase the initial value by the new value
			self.inventory[product] += qty
		else:
			self.inventory[product] = qty # if value is 0 append the new value to 0

	def print_inventory(self):
		print("Items in Inventory")
		for key, value in self.inventory.items(): #from inventory dict object,
			print(key, value)	# print value string [using/calling name object] return key
		print()