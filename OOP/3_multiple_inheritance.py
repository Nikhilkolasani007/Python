class A:
    def method_a(self):
        print("Method from class A")

class B:
    def method_b(self):
        print("Method from class B")

class C(A, B):  # Subclass inheriting from classes A and B
    pass

# Creating an instance of class C
obj = C()

# Calling methods from both superclasses
obj.method_a()  # Output: Method from class A
obj.method_b()  # Output: Method from class B
