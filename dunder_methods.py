class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: Rs. {self.price}"

    def __repr__(self):
        return (
            f"Product(name={self.name!r}, "
            f"price={self.price}, quantity={self.quantity})"
        )

    def __len__(self):
        return self.quantity

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price == other.price

    def __add__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price + other.price


# Creating objects
laptop = Product("Laptop", 80000, 5)
phone = Product("Phone", 50000, 3)
another_laptop = Product("Gaming Laptop", 80000, 2)

# Testing special methods
print("String representation:", laptop)
print("Developer representation:", repr(laptop))
print("Available quantity:", len(laptop))
print("Same price:", laptop == another_laptop)
print("Combined price:", laptop + phone)
