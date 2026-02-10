import math
import random

# Task 1: Store 7 different numbers in a list and print their sum
numbers = [12, 45, 7, 23, 89, 34, 56]
print("Task 1 - Numbers:", numbers)
print("Sum of the numbers:", sum(numbers))
print("-" * 40)

# Task 2: Round pi to 2 decimal places
num = math.pi
rounded_pi = round(num, 2)
print(f"Task 2 - Value of pi: {num}")
print(f"Pi rounded to 2 decimal places: {rounded_pi}")
print("-" * 40)

# Task 3: Given list of letters, print the length
letters = ["a", "b", "c", "d", "e", "f"]
length = len(letters)
print("Task 3 - List of letters:", letters)
print("Length of the list:", length)
print("-" * 40)

# Task 4: Display absolute value of a number (given num = 72)
num = 72
absolute_value = abs(num)
print(f"Task 4 - Number: {num}")
print(f"Absolute value: {absolute_value}")
# Just to show it works with negative numbers too:
print(f"Absolute value of -72: {abs(-72)}")
print("-" * 40)

# Task 5: Guessing game
print("Task 5 - Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

secret_number = random.randint(1, 100)
attempts = 0
guessed_correctly = False

while True:
    guess_input = input("\nEnter your guess (or type 'quit' to give up): ")
    
    if guess_input.lower() == 'quit':
        print(f"You gave up! The secret number was {secret_number}")
        break
    
    try:
        guess = int(guess_input)
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed it!")
            print(f"The number was {secret_number}")
            print(f"It took you {attempts} attempt(s)!")
            guessed_correctly = True
            break
            
    except ValueError:
        print("Please enter a valid number or 'quit'")

print("-" * 40)

# Task 6: Function that takes two numbers and returns their product
def multiply_two_numbers(a, b):
    return a * b

# Example usage
num1 = 8
num2 = 9
result = multiply_two_numbers(num1, num2)

print(f"Task 6 - Multiplication function")
print(f"{num1} × {num2} = {result}")

# Bonus: Test the function with user input
print("\nBonus: Let's multiply two numbers you choose!")
try:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print(f"{x} × {y} = {multiply_two_numbers(x, y)}")
except ValueError:
    print("Invalid input, but the function works!")

print("\nAll tasks completed!")