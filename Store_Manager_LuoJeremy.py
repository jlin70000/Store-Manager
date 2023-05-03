#IDLE Open Source
#Note to Viewer: The code uses a dictionary named 'inventory' to store product names as keys and their corresponding prices and quantities as values.
#The dictionary is used throughout the program to keep track of the products, their prices and quantities, and to perform different operations on them, such as searching, adding, updating, and removing products.
#For example, when printing the inventory, the program iterates over the dictionary and accesses the data for each product using the items() method of the dictionary. When adding a new product, the program inserts a new key-value pair into the dictionary.
#When updating an existing product, the program modifies the values of the corresponding key in the dictionary. And when removing a product, the program removes the corresponding key-value pair from the dictionary using the del statement.
#Jeremy Luo


inventory = {
    'soft drink': [0.99, 10],
    'onion rings': [1.29, 5],
    'small fries': [1.49, 20]
}

#function prints the inventory in a table format.
def print_inventory():
    print("Product".ljust(15), "Price".rjust(8), "Quantity".rjust(8))
    for product, data in inventory.items():
        price, quantity = data
        print(product.ljust(15), str(price).rjust(8), str(quantity).rjust(8))
        
#function prompts the user for a product name and prints the price of the product if the product is in the inventory.
def search_product():
    product_name = input("Enter a product name: ")
    if product_name in inventory:
        price, quantity = inventory[product_name]
        print("We sell '{}' at {} per unit".format(product_name, price))
    else:
        print("Sorry, we don't sell '{}'".format(product_name))

#function prompts the user for a new product name, price, and quantity, and adds it to the inventory.
def add_product():
    product_name = input("Enter a product name: ")
    if product_name in inventory:
        print("Duplicate product name")
        return
    price = None
    while price is None:
        try:
            price = float(input("Enter a price: "))
            if price < 0:
                print("Invalid range, try again")
                price = None
        except ValueError:
            print("Invalid input, try again")
    quantity = None
    while quantity is None:
        try:
            quantity = int(input("Enter an inventory amount: "))
            if quantity < 0:
                print("Invalid range, try again")
                quantity = None
            elif quantity > 100:
                print("Invalid range, try again")
                quantity = None
        except ValueError:
            print("Invalid input, try again")
    inventory[product_name] = [price, quantity]
    print("Product added")
    
#function prompts the user for a product name and removes it from the inventory if the product exists.
def remove_product():
    product_name = input("Enter a product name: ")
    if product_name not in inventory:
        print("Unknown product name")
        return
    del inventory[product_name]
    print("Product removed")
# function prompts the user for a product name and what to update, its name, price, or quantity, and makes the corressponding change to the inventory.
def update_product():
    product_name = input("Enter a product name: ")
    if product_name not in inventory:
        print("Unknown product name")
        return
    print("(n)ame, (p)rice or (a)mount?" , end="")
    option = input().strip().lower()
    if option == "n":
        new_name = input("Enter a new name: ")
        inventory[new_name] = inventory.pop(product_name)
        print("Product renamed")
    elif option == "p":
        price = None
        while price is None:
            try:
                price = float(input("Enter a new price: "))
                if price < 0:
                    print("Invalid range, try again")
                    price = None
            except ValueError:
                print("Invalid input, try again")
        inventory[product_name][0] = price
        print("Product price updated")
    elif option == "a":
        quantity = None
        while quantity is None:
            try:
                quantity = int(input("Enter a new inventory amount: "))
                if quantity < 0:
                    print("Invalid range, try again")
                    quantity = None
                elif quantity > 100:
                    print("Invalid range, try again")
                    quantity = None
            except ValueError:
                print("Invalid input, try again")
        inventory[product_name][1] = quantity
        print("Product inventory updated")
    else:
        print("Unknown command, try again")

#function provides a report that includes the total cost of all items in the inventory, the highest priced item, and the lowest priced item.
def report():
    total_cost = 0
    highest_price = 0
    highest_price_product = ""
    lowest_price = float('inf')
    lowest_price_product = ""
    for product_name in inventory:
        price, quantity = inventory[product_name]
        total_cost += price * quantity
        if price > highest_price:
            highest_price = price
            highest_price_product = product_name
        if price < lowest_price:
            lowest_price = price
            lowest_price_product = product_name
    print(f"Total cost of all items in inventory: {total_cost:.2f}")
    print(f"Highest priced item: {highest_price:.2f} is {highest_price_product}")
    print(f"Lowest priced item: {lowest_price:.2f} is {lowest_price_product}")

#main program uses while loop
while True:
    print("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ", end="")
    choice = input().strip().lower()
    if choice == "q":
        print('See you soon!')
        break
    elif choice == "s":
        search_product()
    elif choice == "l":
        print_inventory()
    elif choice == "a":
        add_product()
    elif choice == "r":
        remove_product()
    elif choice == "u":
        update_product()
    elif choice == "e":
        report()
    #make sure user inputs appropriate letters
    else:
        print("Unknown command, try again")
