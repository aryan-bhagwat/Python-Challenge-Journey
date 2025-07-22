# Day 18: Tuples in Python


## 1. What Is a Tuple?

# A tuple is an ordered, immutable collection of items. You can’t change the items after creation.
my_tuple = (1, 2, 3)
# ✅ Allows duplicates
# ❌ Cannot change, add, or remove elements after creation


## 2. Why Use Tuples Instead of Lists?

# Tuples use less memory than lists
# Tuples can be used as dictionary keys
# Ensures data safety — fixed data structures like (x, y) coordinates, date of birth, etc.


## 3. Creating Tuples
t1 = (1, 2, 3)
t2 = ("Python", True, 3.14)
t3 = (1,)  # Single-element tuple requires a comma
print(t1, t2, t3)


##  4. Accessing Tuple Elements
my_tuple = (10, 20, 30, 40)

print(my_tuple[0])      # 10
print(my_tuple[-1])     # 40
print(my_tuple[1:3])    # (20, 30)


## 5. Tuple Packing and Unpacking

# Packing
person = ("Aryan", 20, "India")

# Unpacking
name, age, location = person
print(name, age, location)


##  6. Tuple Operations
a = (1, 2)
b = (3, 4)

print(a + b)
print(a * 2)
print(3 in b)


## Basic Practice

# 1. Create a tuple of your:
'''
1. Name
2. Age
3. Location

Then unpack and print each value.
'''
# person = ("Aryan", 20, "India")
# name, age, location = person
print(name)
print(age)
print(location)

# 2. Create a tuple of numbers and:
'''
Print min, max, sum, and average
'''
numbers = (65,36,43,7,35,4)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(sum(numbers) / len(numbers))


## Intermediate Practice

# 1. Convert this list to a tuple and check its type:
languages = ["Python", "Java", "C++"]

tuple_ = tuple(languages)
print(tuple_)

# 2. Write a function that takes a tuple of 3 elements and returns the sum.
def sum_of_tuple():
    nums = []
    for i in range(3):
        tuple_input = int(input(f"Enter {i+1} number: "))
        nums.append(tuple_input)
    sum_tuple = tuple(nums)
    return sum(sum_tuple)
    
print(f"Sum of 3 numbers is {sum_of_tuple()}")


## Bonus Challenge : Student Info System

student = ("Aryan", 22, "Data Science", 92.5)
stu_name, stu_age, stu_field, stu_marks = student

print(f"Student Name: {stu_name}")
print(f"Age: {stu_age}")
print(f"Field: {stu_field}")
print(f"Marks: {stu_marks}")

def grade():
    if stu_marks > 90:
        return "Grade: Excellent"
    
print(grade())