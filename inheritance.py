class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def show_developer_details(self):
        self.show_details()
        print(f"Programming Language: {self.programming_language}")


developer = Developer("Mohib", 50000, "Python")

developer.show_developer_details()
