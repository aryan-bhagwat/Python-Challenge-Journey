# Day 13 : Function Scope – Local vs Global Variables

## 1. Define a local variable inside a function and try to print it outside (observe the error).
def error():
    count = 1
    print(f"Local Variable: {count}")

error()
# print(count) # This will display an error

## 2. Create a global variable, access it in a function without modifying.
count = 1

def global_var():
    print(count)

global_var()


## 3. Create a global counter and modify it inside a function using global.
def global_modify():
    global count
    count += 1

global_modify()
print(count)


## Intermediate Practice : Compare Local and Global

x = 10
def change():
    x = 5
    print("Inside function:", x)

change()
print("Outside function:", x)

# Now add global x inside the function — what changes?
x = 10

def global_change():
    global x
    x = 5
    print(f"Inside Function: {x}")

global_change()
print(f"Outside Function: {x}")


## Basic Practice

# Global Counter with User Input

visits = 0

def track_visit():
    global visits
    visits += 1
    print("Visit recorded!")

while True:
    user = input("Do you want to visit the site?(yes/no): ")
    if user == "yes":
        track_visit()
    elif user == "no":
        print("No more visits.")
        break
    else:
        print("Please enter 'yes' or 'no'.")

print(f"Total visits: {visits}")