from ecommerce import Customer, Product, Inventory
from collections import  OrderedDict
import os
import sys


def clear():
	os.system("cls" if os.name == "nt" else "clear")


def quit():
	"""Quit"""
	sys.stdout.write("THANK YOU FOR USING THIS SCRIPT\n")
	sys.exit(1)


def test():
	print("name:", customer.name)
	print("email", customer.email)
	print()


	mobile = Product("iPhoneX", 5000)

	pc = Product("Dell-Latitude", 2000)


	inventory = Inventory()
	inventory.add_inventory(mobile, 95)
	inventory.add_inventory(pc, 20)
	inventory.print_inventory()

	customer.add_product(inventory, mobile)
	customer.add_product(inventory, pc)
	customer.print_purchases()
	inventory.print_inventory()


def inventory():
	"""Inventory"""
	inventory = Inventory()

	print("Add Product and Quantity")
	product = input("Enter Product: ")
	qty = int(input("Enter Quantity: "))

	inventory.add_inventory(product, qty)

	clear()
	print("Inventory is updated successful")

	view = input("Do you want to view inventory? N/y: ")

	if view in ["N", "n"]:
		main()
	elif view == "":
		main()
	elif view in ["Y", "y"]:
		inventory.print_inventory()

	input("Press enter to go back the main menu")
	main()


def product():
	"""Product"""
	name = input("Product Name:" )
	price = input("Product Price:" )


def customers():
	"""Customer"""
	name = input("Customer Name: ")
	email = input("Customer Email: ")

	customer = Customer(name, email)
	print("Customer info saved")
	clear()

	customer.add_product()
	print("Customer purchases are:")
	customer.print_purchases()


def main():
	print("Select option")
	for key, value in menu.items():
		print(f"[{key}] {value.__doc__}")

	option = input("\n>>> ")
	if option == list(menu.keys())[0]:
		customers()
	elif option == list(menu.keys())[1]:
		product()
	elif option == list(menu.keys())[-2]:
		inventory()
	elif option == list(menu.keys())[-1]:
		quit()


menu = OrderedDict([
	["c", customers],
	["p", product],
	["i", inventory],
	["q", quit]
])


if __name__ == "__main__":
	main()