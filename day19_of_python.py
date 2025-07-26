# # Day 19 : Advanced Function Techniques in Python

# ## 1. *args – Variable Number of Positional Arguments
# def add_all(*args):
#     return sum(args)

# print(add_all(2,4,6,7))


# # 2. **kwargs – Variable Number of Keyword Arguments
# def print_details(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")
    
# print_details(Name = "Aryan", Age = 20, Course = "Python")

# # 3. Combine *args and **kwargs
# def student_info(*args, **kwargs):
#     print("Args : ", args)
#     print("Kwargs : ", kwargs)

# student_info("Aryan", "India", Age = 20, Course = "Python")

# # 4. Nested Functions
# def outer():
#     def inner():
#         print("This is inner function")
#     inner()
#     print("This is outer function")
# outer()

# # 5. Recursion
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(4))


## Basic Practice

# 1. Write a function multiply_all(*args) that returns the product of all arguments.
def multiply_all(*args):
    total = 1
    for i in args:
        total *= i
    return total
print(multiply_all(5,2,3))

# 2. Write a function print_info(**kwargs) that prints key-value pairs from kwargs.
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
print_info(Name = "Aryan", Location = "India", Phone = "2345676545")


## Intermediate Practice

# 1. Write a recursive function sum_digits(n) that returns the sum of digits of a number.
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)
print(sum_digits(745))

# 2. Create a function profile(name, *hobbies, **details) and print them all.
def profile(name, *hobbies, **details):
    print(f"Name : {name}")
    print("Hobbies: ")
    for hobby in hobbies:
        print(f"- {hobby}")
    print("\nDetails: ")
    for key, value in details.items():
        print(f"{key} : {value}")
profile("Aryan", "Cricket", "Badminton", "Video editing", Cricket = "I Play Cricket Daily", Badminton = "I played twice in a week", Video_editing = "Based on client needs")


## Bonus Challenge : Recursive Palindrome Checker

# Write a recursive function to check if a string is a palindrome: 
# Hint: Use s[1:-1] and compare s[0] with s[-1]

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("cacoc"))  # False
print(is_palindrome("madam"))  # True
print(is_palindrome("python")) # False