# Day 11 : Loop Control – break, continue, else

## 1. break - Exit early
for i in range(1,10):
    if i == 5:
        break # Exit the loop when i is 5
    print(i)
print("\n")

## 2. continue – Skip Current Iteration
for i in range(1,6):
    if i == 3:
        continue # Skip the iteration when i is 5
    print(i)
print("\n")

## 3. Else with Loops
for i in range(1,5):
    print(i)
else:
    print("Loop completed without break")
print("\n")

## Now with break:
for i in range(1,5):
    if i == 3:
        break # Exit the loop when i is 3
    print(i)
else:
    print("This will not be printed because of break")
print("\n")


## Basic Practice

# 1. Print numbers 1 to 10, but stop if the number is 6 using break.

for i in range(1,10):
    if i == 6:
        break # Exit the loop when i is 6
    print(i)
print("\n")

# 2. Print numbers 1 to 10, but skip 4 and 7 using continue.
for i in range(1, 11):
    if i == 4 or i == 7:
        continue # Skip the iteration when i is 4 or 6
    print(i)
print("\n")


## Intermediate Practice : Login System

'''
1. Store a secret password
2. Give the user 3 chances to enter the correct password using while
3. Break if correct
4. Else (after 3 tries) print “Access Denied"
'''

password = "Aryan123"

attempts = 3

while attempts > 0:
    user_input = input("Enter your password: ")
    if user_input == password:
        print("Access Granted")
        break
    else:
        attempts -= 1
        print(f"Incorrect password. You have {attempts} attempts left.")


## Bonus Challenge : Prime Number Checker with Loop Else

num = int(input("Enter a number: "))

for i in range(2, num):
    if num % i == 0:
        print("Not prime")
        break
else:
    print("Prime number")