class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Usage
dog = Dog()
print(dog.speak())  # Output: Woof!

cat = Cat()
print(cat.speak())  # Output: Meow!
