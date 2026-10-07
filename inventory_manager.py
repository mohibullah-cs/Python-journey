inventory = {
    "Laptop": 5,
    "Mouse": 10,
    "Keyboard": 7,
    "Headphones": 4
}

print("Current Inventory:")

for item, quantity in inventory.items():
    print(f"{item}: {quantity}")

item = input("\nEnter item name: ")

if item in inventory:
    quantity = int(input("Enter quantity to add: "))
    inventory[item] += quantity
    print(f"{item} updated successfully!")
else:
    quantity = int(input("Enter quantity: "))
    inventory[item] = quantity
    print(f"{item} added successfully!")

print("\nUpdated Inventory:")

for item, quantity in inventory.items():
    print(f"{item}: {quantity}")
