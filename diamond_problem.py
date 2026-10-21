class A:
    def show(self):
        print("Method from class A")


class B(A):
    def show(self):
        print("Method from class B")
        super().show()


class C(A):
    def show(self):
        print("Method from class C")
        super().show()


class D(B, C):
    def show(self):
        print("Method from class D")
        super().show()


obj = D()

obj.show()

print("\nMethod Resolution Order:")
print([cls.__name__ for cls in D.mro()])
