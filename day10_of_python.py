#  Day 10 : Loops in Python – for & while

## 1. For Loop

# 0 to 4
for i in range(5):
    print("Hello", i)

# 2 to 5
for i in range(2, 6):
    print("Hello", i)

# 1 to 9 (step = 2)
for i in range(1, 10, 2):
    print("Hello", i)

print("\n")


## 2. While Loop

# Using a while loop to print "Hello" 5 times
count = 1
while count <= 5:
    print("Hello", count)
    count += 1

print("\n")


## Loop control statements

# 1. Break statement

for i in range(3):
    if i == 2:
        break # Exit the loop when i is 2
    print("Hello", i)

print("\n")

# 2. Continue statement

for i in range(5):
    if i == 1:
        continue # Skip the iteration when i is 1
    print("Hello", i)

print("\n")

# 3. Else statement with loops

for i in range(3):
    print("Hello", i)
else:
    print("Loop completed without break")


## Basic Practice

# 1. Print numbers from 1 to 10 using a for loop and while loop

for i in range(1, 11):
    print(i, end=" ")

print("\n")

count = 1 
while count <=10:
    print(count,end=" ")
    count += 1

print("\n")

# 2. Print even numbers from 1 to 20 using a for loop and while loop

for i in range(2, 21, 2):
    print(i, end=" ")

print("\n")

count = 1 
while count <= 20:
    if count % 2 == 0 :
        print(count, end= " ")
    count += 1


## Intermidiate Practice

# 1. Print the multiplication table of a number using for loop and while loop
table = int(input("Enter a number for multiplication table: "))

for i in range(1, 11):
    print(f"{table} x {i} = {table * i}")

count = 1

while count <= 10:
    print(f"{table} x {count} = {table * count}")
    count += 1

# 2. Print sum of numbers from 1 to n

n = int(input("Enter a number to find the sum from 1 to n: "))

total = 0

for i in range(1, n + 1):
    total += i  

print(f"The sum of numbers from 1 to {n} is: {total}")

n = int(input("Enter a number to find the sum from 1 to n using while loop: "))

total = 0

count = 0

while count <= n:
    total += count
    count += 1
print(f"The sum of numbers from 1 to {n} using while loop is: {total}")

# 3. Print all characters of a word using for char in word

word = input("Enter a word to print all characters: ")

for char in word:
    print(char, end=" ")

# 3. Print all characters of a word using while loop

count = 0

while count < len(word):
    print(word[count], end=" ")
    count += 1

    
## Bonus Challenge : Number Guessing Game using loops

import random

random_number = random.randint(1,10)
guess = int(input("Guess a number between 1 and 10: "))

while guess != random_number:
    if guess < random_number:
        print("Too Low")
    elif guess > random_number:
        print("Too High")
    guess = int(input("Try again! Guess a number between 1 and 10: "))
print("Congratulations! You've guessed the number:", random_number)