# Day 17: Sets and Set Operations in Python

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # Union → {1, 2, 3, 4, 5}
print(a & b)   # Intersection → {3}
print(a - b)   # Difference → {1, 2}
print(a ^ b)   # Symmetric Difference → {1, 2, 4, 5}


## Basic Practice

# 1. Create a set of your top 5 favorite numbers and add/remove a number.
s = {32,42,63,54,35}

s.add(34)
s.remove(42)
s.discard(32)
print(s)

# 2. Remove duplicates from this list using a set:
nums = [1, 2, 2, 3, 4, 4, 5]

num = list(set(nums))
print(nums)
print(num)


## Intermediate Practice

# 1. Find union, intersection, and symmetric difference. Check if a is a subset of {1, 2, 3, 4, 5}
a = {1, 2, 3, 4}  
b = {3, 4, 5, 6}
subset_of = {1,2,3,4,5}

print(a | b)
print(a & b)
print(a ^ b)
print(a.issubset(subset_of))

# 2. Write a program to input 5 fruits and keep only unique ones.
fruits = []
for i in range(5):
    value = input(f"Enter {i+1} Fruit name: ")
    fruits.append(value)
print(list(set(fruits)))


## Bonus Challenge : Unique Word Extractor

text = "Python is fun and python is powerful"
words = text.lower().split()
unique = set(words)
print(unique)