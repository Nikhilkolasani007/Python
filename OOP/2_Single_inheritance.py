class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an instance of the Person class
person1 = Person("Alice", 30)

# Accessing attributes and calling methods of the object
print(person1.name)      # Output: Alice
print(person1.age)       # Output: 30
person1.introduce()      # Output: Hello, my name is Alice and I am 30 years old.
