# Day 12 : Functions in Python – def, Parameters, return


## 1. Defining a function
def greet():
    print("Hello, Aryan!")

greet()

## 2. Function with Parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Aryan")

## Multiple parameters:
def add(a,b):
    print(f"Addition of a and b is {a + b}!")

add(6,4)

## 3. Return Statement
def multiply(a,b):
    return a * b

result = multiply(6,4)
print(f"Multiplication of a and b is {result}!")

## 4. Default Parameters
def greet(name = "Guest"):
    print(f"Hello, {name}!")

greet()
greet("Aryan")


## Basic Practice

# 1. Write a function to add two numbers
def add(a,b):
    print(f"Addition of two numbers is: {a + b}!")

add(2,6)

# 2. Write a function to greet a person by name
def greet(name):
    print(f"Hello, {name}!")

greet("Aryan")


## Intermediate Practice

# 1. Create a function to: 1. Calculate the square of a number 2. Return the result
def square(a):
    return a * a

result = square(6)
print(f"Square is {result}!")

# 2. Create a function is_even(n) → return True/False
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
print(is_even(6))
print(is_even(7))

# 3. Create a function to return the maximum of three numbers
def max(a,b,c):
    if a > b:
        return f"{a} is maximum"
    elif b > c:
        return f"{b} is maximum"
    elif c > a:
        return f"{c} is maximum"

print(max(1,9,5))


## Bonus challenge :  Simple Calculator Using Functions

def add(a,b):
    return f"{a + b}"

def sub(a,b):
    return f"{a - b}"

def multiple(a,b):
    return f"{a * b}"

def div(a,b):
    return f"{a / b}"

def calculator():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    op = input("Choose operator(+, -, *, /): ")

    if op == "+":
        print(f"Addition: {add(a,b)}")
    elif op == "-":
        print(f"Subtraction: {sub(a,b)}")
    elif op == "*":
        print(f"Multiplication: {multiple(a,b)}")
    elif op == "/":
        print(f"Division: {div(a,b)}")
    else:
        print("This is not correct operator")
    
calculator()