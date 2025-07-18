# Day 3 - User Input, Output & Type Casting

## Basic practice

name = input("What is your name? ") # This takes user input for name
age = input("How old are you? ") # This takes user input for age
height = input("What is your height in feet? ") # This takes user input for height

print("Hello", name,", you are", age, "years old and", height, "feet tall.") # This prints a greeting with user input

## Intermediate practice

add = int(input("Enter a number to add 10: ")) # This takes user input and converts it to an integer
add += 10 # This adds 10 to the input number
print("The sum is:", add) # This prints the result of the addition

subtract = int(input("Enter a number to subtract 10: ")) # This takes user input and converts it to an integer
subtract -= 10 # This subtracts 10 from the input number
print("The difference is:", subtract) # This prints the result of the subtraction

multiply = int(input("Enter a number to multiply by 10: ")) # This takes user input and converts it to an integer
multiply *= 10 # This multiplies the input number by 10
print("The product is:", multiply) # This prints the result of the multiplication

divide = int(input("Enter a number to divide by 10: ")) # This takes user input and converts it to an integer
divide /= 10 # This divides the input number by 10
print("The quotient is:", divide) # This prints the result of the division