# Day 15 : List Comprehension in Python

## List Comprehension:
squares = [x * x for x in range(5)]
print(squares)
## Example:
names = ["Aryan", "Manish", "Chetan", "Ganesh", "Yun"]
upper_name = [i.upper() for i in names]
print(upper_name)

## With Condition (if clause)
nums = [1, 2, 3, 4, 5, 6]
evens = [x for x in nums if x % 2 == 0]
print(evens)

## With if-else Inside Expression
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
print(labels) 


## Basic Practice

# Create a list of squares of numbers from 1 to 10 using list comprehension
squares = [x * x for x in range(1,11)]
print(squares)

# Convert a list of words to uppercase.
# names = ["Aryan", "Manish", "Chetan", "Ganesh"]
uppercase = [i.upper() for i in names]
print(uppercase)


## Intermediate Practice

# Filter all words longer than 4 characters from a list.

word = [name for name in names if len(name) > 4]
print(word)

# Replace each number in a list with "Even" or "Odd".
x = [2,6,8,3,6,3,7,3]
num = ["Even" if n % 2 == 0 else "Odd" for n in x]
print(num)

# Convert temperatures from Celsius to Fahrenheit using:
temps_c = [36.6, 37.8, 38.2]
fahrenheit = [i * 1.8 + 32 for i in temps_c]
print(fahrenheit)


## Bonus Challenge : Flatten a Matrix

matrix = [
    [1, 2, 3],
    [4, 5],
    [6]
]

flatten = [i for nums in matrix for i in nums]
print(flatten)