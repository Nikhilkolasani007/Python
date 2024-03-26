class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the '+' operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Overloading the '*' operator
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v1 = Vector(2, 4)
v2 = Vector(1, 3)

# Using operator overloading
v3 = v1 + v2
v4 = v1 * 3

print(f"v3: ({v3.x}, {v3.y})")  # Output: v3: (3, 7)
print(f"v4: ({v4.x}, {v4.y})")  # Output: v4: (6, 12)
