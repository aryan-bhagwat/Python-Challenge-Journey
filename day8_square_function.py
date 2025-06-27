# Day 8 Challenge: Create a function that returns the square of a number

def square(num):
    return num ** 2

# Get user input and print the result
value = int(input("Enter a number: "))
result = square(value)
print(f"The square of {value} is {result}.")
