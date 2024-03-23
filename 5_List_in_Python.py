# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]

# Creating a list of strings
fruits = ["apple", "banana", "cherry"]

# Creating a list of mixed data types
mixed_list = [1, "hello", 3.14, True]

print(numbers)
print(fruits)
print(mixed_list)


# Accessing Elements
fruits = ["apple", "banana", "cherry"]

print(fruits[0])   # Output: "apple"
print(fruits[-1])  # Output: "cherry"

# Slicing Elements

numbers = [1, 2, 3, 4, 5]

print(numbers[1:4])  # Output: [2, 3, 4]


# Modifying List

numbers = [1, 2, 3, 4, 5]

# Changing an element
numbers[0] = 10
print(numbers)  # Output: [10, 2, 3, 4, 5]

# Appending an element
numbers.append(6)
print(numbers)  # Output: [10, 2, 3, 4, 5, 6]

# Removing an element
numbers.remove(3)
print(numbers)  # Output: [10, 2, 4, 5, 6]

# Extend an Elements
numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print(numbers)  # Output: [1, 2, 3, 4, 5, 6]

# Insertion using Index
numbers = [1, 2, 3]
numbers.insert(1, 4)
print(numbers)  # Output: [1, 4, 2, 3]

# Remove Element
numbers = [1, 2, 3, 2]
numbers.remove(2)
print(numbers)  # Output: [1, 3, 2]

# Pop Index
numbers = [1, 2, 3]
print(numbers.pop())  # Output: 3
print(numbers)  # Output: [1, 2]

# Sort
numbers = [3, 1, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3]

# reverse
numbers = [1, 2, 3]
numbers.reverse()
print(numbers)  # Output: [3, 2, 1]

