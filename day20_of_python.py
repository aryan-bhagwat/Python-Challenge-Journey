# Day 20 : File Handling in Python

## 1. Opening files:
file = open("test.txt", "r+")
content = file.read()
file.close()
print(content)

## 2. File Modes:

# r = Read(default)
# w = Write(overwrite)
# a = Append
# x = Create new file(Fails if exists)
# r+ = Read and Write

## 3. Using with (Automatically closes the file after use):
with open("test.txt", "r") as file:
    content = file.read()
    print(content)

## 4. Writing to files:
with open("newfile.txt", "w") as file:
    file.write("Hello, Aryan!\n")
    file.write("Welcome to Day 20")

## 5. Appending to files:
with open("newfile.txt", "a") as file:
    file.write("\nThis is an extra line.")

## 6. Reading line by line:
with open("newfile.txt", "r") as file:
    for line in file:
        print(line.strip())


## Basic Practice

# 1. Create a file data.txt and write your name, age and location in it.
# 2. Read the file and print its contents line-by-line
with open("data.txt", "r+") as file:
    file.write("Name : Aryan\n")
    file.write("Age : 20\n")
    file.write("Location : Navi Mumbai\n")
    file.write("\nName : Aryan\nAge : 20\nLocation : Navi Mumbai")

    file.seek(0) # Move cursor to the beginning before reading
    content = file.read()
    print(content)

    file.seek(0) # Move cursor to the beginning before reading
    for line in file:
        print(line.strip())


## Intermediate Practice:

# 1. Ask the user to enter multiple lines and write them to a file.
with open("file.txt", "w+") as file:
    while True:
        user = input("Enter a line (or exit to stop): ")
        if user.strip().lower() == "exit":
            break
        file.write(user + "\n")
    
    file.seek(0)
    print(f"File Content:\n{file.read()}")

# 2. Write a Python program that copies contents from one file to another
with open("file.txt", "r") as source_file, open("newfile.txt", "a") as dest_file:
    for line in source_file:
        dest_file.write("\n" + line.strip())

print("Content copied from file.txt to newfile.txt successfully")


## Bonus Challenge : Student Logger App

# 1. Ask user input for:
# - Name
# - Course
# - Score
# 2. Save this in a file called students.txt in the format:
# Name: Aryan
# Course: Python
# Score: 95
# .........

# Let user enter multiple students using a loop, and stop when they type "exit":

with open("studuent.txt", "a+") as file:
    while True:
        name = input("Enter Your Name: ")
        if name.strip().lower() == "exit":
            break
        course = input("Enter Your Course: ")
        score = input("Enter Your Score: ")
        print("Enter exit when you done")
        
        file.write(f"\n\nName: {name}\nCourse: {course}\nScore: {score}")

    file.seek(0)
    content = file.read()
    print(content)