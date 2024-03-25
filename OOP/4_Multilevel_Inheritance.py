class Animal:
    def eat(self):
        print("Animal is eating...")

class Dog(Animal):
    def bark(self):
        print("Dog is barking...")

class Labrador(Dog):
    def wag_tail(self):
        print("Labrador is wagging tail...")

# Creating an instance of Labrador
my_labrador = Labrador()

# Calling methods from all levels of inheritance
my_labrador.eat()       # Output: Animal is eating...
my_labrador.bark()      # Output: Dog is barking...
my_labrador.wag_tail()  # Output: Labrador is wagging tail...
