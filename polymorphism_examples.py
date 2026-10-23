from abc import ABC, abstractmethod


# 1. Base Class Method Overriding
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Dog barks"


class Cat(Animal):
    def sound(self):
        return "Cat meows"


# 2. Duck Typing
class PDFDocument:
    def open(self):
        return "Opening PDF document"


class TextDocument:
    def open(self):
        return "Opening text document"


def open_document(document):
    print(document.open())


# 3. Method Overloading using Default Arguments
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c


# 4. Operator Overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


# Testing Polymorphism
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.sound())

open_document(PDFDocument())
open_document(TextDocument())

calculator = Calculator()
print("Two numbers:", calculator.add(10, 20))
print("Three numbers:", calculator.add(10, 20, 30))

v1 = Vector(2, 3)
v2 = Vector(4, 5)
print("Vector addition:", v1 + v2)
