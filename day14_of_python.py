# Day 14 : Lambda Functions in Python

## Write a lambda to add two numbers.
add = lambda x,y : x + y
print(add(2,4))

## Write a lambda to check if a number is even or odd.
even = lambda x : "Even" if x % 2 == 0 else "Odd"
print(even(15))

## Write a lambda to check if a number is even or odd using filter
nums = [4,2,5,8,3]
even = list(filter(lambda x : x % 2 == 0, nums))
print(even)


## Intermediate Practice
 
# Use map() + lambda to: Convert list of temperatures in Celsius to Fahrenheit - Fahrenheit = C * 1.8 + 32
temperature = [56,86,57,96,68,57]
Fahrenheit = list(map(lambda c : c * 1.8 + 32, temperature))
print(Fahrenheit)


# Use filter() + lambda to: Get all names longer than 5 characters from a list
names = ["Aryan", "Lakhan", "Mohan", "Yogi", "Karan", "Yoyo"]
more_names = list(filter(lambda name : len(name) >= 5 , names))

print(f"Names longer than 5 Characters: {more_names}")


# Sort a list of (name, age) tuples by age using lambda in sorted()
list = [("Aryan", 26), ("Lakhan", 45), ("Karan", 43), ("Manoj", 22)]
sort_list = sorted(list, key = lambda x : x[1])
print(sort_list)


## Bonus Challenge : Student Filter System

students = [
    {"name": "Aryan", "marks": 85},
    {"name": "Sana", "marks": 55},
    {"name": "Ravi", "marks": 92}
]

# Filter only students with marks > 60 using filter() and lambda.

marks = list(filter(lambda x : x["marks"] > 60, students))
print(marks)