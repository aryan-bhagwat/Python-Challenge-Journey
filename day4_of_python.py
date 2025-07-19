# Day 4 - Python Operators - Arithmetic, Comparison, Logical

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# Arithmetic Operations

print("Arithmetic Operations:")
print(f"Addition: {x} + {y} = {x + y}")
print(f"Subtraction: {x} - {y} = {x - y}")
print(f"Multiplication: {x} * {y} = {x * y}")
print(f"Division: {x} / {y} = {x / y}")
print(f"Floor Division: {x} // {y} = {x // y}")
print(f"Modulus: {x} % {y} = {x % y}")
print(f"Exponentiation: {x} ** {y} = {x ** y}")

# Comparison Operations

print("\nComparison Operations:")
print(f"Equal to: {x} == {y} -> {x == y}")
print(f"Not equal to: {x} != {y} -> {x != y}")
print(f"Greater than: {x} > {y} -> {x > y}")
print(f"Less than: {x} < {y} -> {x < y}")
print(f"Greater than or equal to: {x} >= {y} -> {x >= y}")
print(f"Less than or equal to: {x} <= {y} -> {x <= y}")

# Logical Operations

print("\nLogical Operations:")
print(f"Logical AND: {x > 0} and {y > 0} -> {x > 0 and y > 0}")
print(f"Logical OR: {x > 0} or {y > 0} -> {x > 0 or y > 0}")
print(f"Logical NOT: not ({x > 0}) -> {not (x > 0)}")


# intermidate practice 

n = int(input("\nWhat is your age? "))

if n < 18:
    print("You are not eligible to vote.")
else:
    print("You are eligible to vote.")


#bonus practice

first_mark = int(input("\nEnter your first mark: "))
second_mark = int(input("Enter your second mark: "))
third_mark = int(input("Enter your third mark: "))

average = (first_mark + second_mark + third_mark) / 3
print(f"Average: {average}")

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 60:
    print("Grade: C")
else:
    print("Fail")
