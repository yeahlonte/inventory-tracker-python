inventory = {}

def add_item(name, quantity):
    inventory[name] = quantity

def update_item(name, quantity):
    if name in inventory:
        inventory[name] += quantity
    else:
        inventory[name] = quantity

def show_inventory():
    print("\nInventory:")
    for item, qty in inventory.items():
        print(f"{item}: {qty}")

while True:
    print("\n1. Add Item\n2. Update Item\n3. Show Inventory\n4. Exit")
    choice = input("Choose option: ")

    if choice == "1":
        name = input("Item name: ")
        qty = int(input("Quantity: "))
        add_item(name, qty)

    elif choice == "2":
        name = input("Item name: ")
        qty = int(input("Quantity to add: "))
        update_item(name, qty)

    elif choice == "3":
        show_inventory()

    elif choice == "4":
        break
