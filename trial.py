# Basic Python script demonstrating various features

# Variables and printing
name = "Alice"
age = 25
print(f"Hello, {name}! You are {age} years old.")

# Basic arithmetic
a = 10
b = 20
print("Sum:", a + b)
print("Difference:", b - a)
print("Product:", a * b)
print("Division:", b / a)

# Lists and loops
fruits = ["apple", "banana", "cherry", "date"]
print("\nFruits list:")
for fruit in fruits:
    print(f"- {fruit}")

# Conditional statements
print("\nConditional checks:")
if age > 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Functions
def greet(name):
    return f"Hello, {name}!"

print("\nFunction output:")
print(greet("Bob"))

# Dictionaries
person = {"name": "Charlie", "age": 30, "city": "New York"}
print("\nDictionary:")
for key, value in person.items():
    print(f"{key}: {value}")


# List comprehension
print("\nSquares of numbers from 1 to 5:")
squares = [x**2 for x in range(1, 6)]
print(squares)

# Exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("\nException: Cannot divide by zero!")

# Class and object
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"The {self.name} says {self.sound}!")

print("\nClass and object:")
dog = Animal("dog", "woof")
dog.make_sound()

print("\nEnd of script.")
