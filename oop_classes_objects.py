class Student:
    def __init__(self, name, age, marks):
        # Constructor initializes object attributes
        self.name = name
        self.age = age
        self.marks = marks

    def display_info(self):
        # Instance method
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")

    def has_passed(self):
        return self.marks >= 50


# Creating objects
student1 = Student("Mohib", 22, 85)
student2 = Student("Ali", 21, 42)

# Calling methods
student1.display_info()
print(f"Passed: {student1.has_passed()}")

print()

student2.display_info()
print(f"Passed: {student2.has_passed()}")
