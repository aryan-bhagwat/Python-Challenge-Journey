# Day 21 : Exception Handling in Python

## 1. Try and Except
try:
    x = int(input("Enter a number: "))
    print("You entered:", x)
except ValueError:
    print("That's not a valid number!")

## 2. Multiple Exceptions
try:
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Please enter valid integers!")

## 3. Else Clause
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    print("You entered:", num)

## 4. Finally Clause
try:
    file = open("data.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found.")
finally:
    print("Cleaning up...")

## 5. Raise Your Own Errors
x = -5
if x < 0:
    raise ValueError("x cannot be negative!")


## Basic Practice :

# 1. Write a program that asks the user for an integer and handles non-integer input.
try:
    num = int(input("Enter an integer: "))
    print(f"You entered: {num}")
except ValueError:
    print("That was not a valid integer. Please try again.")


# 2. Try to open a file that may not exist and print a helpful message.
filename = input("Enter the filename to open: ")

try:
    with open(filename, 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("File not found. Please check the name and try again.")


## Intermediate Practice :

# Create a calculator that handles:
# ZeroDivisionError
# ValueError
# Any other unexpected error with except Exception as e:

def calculator():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        else:
            print("Invalid operator!")
            return

        print(f"Result: {result}")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter valid numbers.")
    except Exception as e:
        print(f"Unexpected error: {e}")

calculator()


## Bonus Challenge : Student Score Reader

# 1. Ask the user to input a filename (e.g. students.txt)
# 2. Use try to open the file and print its content.
# 3. If the file doesn't exist, show "No such file found!"

def read_student_scores():
    filename = input("Enter the filename (e.g., students.txt): ")
    try:
        with open(f"{filename}", 'r') as file:
            print(file.read())

    except FileNotFoundError:
        print("No such file found!")

read_student_scores()
