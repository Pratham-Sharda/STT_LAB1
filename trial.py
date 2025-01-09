"""
This module demonstrates basic Python functionality including variables, loops,
conditionals, functions, and classes.
"""

NAME = "Alice"  # Updated to follow UPPER_CASE naming style
AGE = 25

def greet_user(user_name: str) -> str:
    """Returns a greeting message for the given name."""
    return f"Hello, {user_name}! You are {AGE} years old."

def arithmetic_operations(num1: int, num2: int) -> None:
    """
    Performs basic arithmetic operations on two numbers and prints the results.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.
    """
    print("Sum:", num1 + num2)
    print("Difference:", num2 - num1)
    print("Product:", num1 * num2)
    print("Division:", num2 / num1)

def display_fruits(fruit_list: list) -> None:
    """
    Displays the list of fruits.

    Args:
        fruit_list (list): A list of fruits to display.
    """
    print("\nFruits list:")
    for fruit in fruit_list:
        print(f"- {fruit}")

class Animal:
    """Represents an animal with a name and a sound."""

    def __init__(self, animal_name: str, sound: str) -> None:
        """
        Initializes the Animal class.

        Args:
            animal_name (str): The name of the animal.
            sound (str): The sound the animal makes.
        """
        self.animal_name = animal_name
        self.sound = sound

    def make_sound(self) -> None:
        """Prints the sound of the animal."""
        print(f"The {self.animal_name} says {self.sound}!")

    def change_name(self, new_name: str) -> None:
        """Changes the name of the animal."""
        self.animal_name = new_name
        print(f"The animal's name has been changed to {self.animal_name}.")

if __name__ == "__main__":
    print(greet_user(NAME))

    # Perform arithmetic operations
    NUM1, NUM2 = 10, 20  # Updated to follow UPPER_CASE naming style
    arithmetic_operations(NUM1, NUM2)

    # Display fruits
    FRUITS = ["apple", "banana", "cherry"]
    display_fruits(FRUITS)

    # Demonstrate class usage
    dog = Animal("dog", "woof")
    dog.make_sound()

    # Changing the animal's name
    dog.change_name("puppy")
    dog.make_sound()
