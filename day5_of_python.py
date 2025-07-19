# Day 5 : String Manipulation in Python

text = "Hello, Aryan"

# Indexing
text[0] # First character

# Negative indexing
text[-1]  # Last character

# Slicing
text[0:5]  # First five characters

# Step slicing
text[::2] # Every second character

# More Slicing Examples
text[1:5]  # From index 1 to 5
text[1:10:2]  # From index 1 to 10, every second character
text[1:]  # From index 1 to the end
text[:5]  # From the start to index 5
text[-5:]  # Last five characters
text[-5:-1]  # From the fifth last to the second last character
text[::-1]  # Reverse the string

# Basic Practice

name = "Aryan Bhagwat"

print(name.upper())  # Convert to uppercase
print(name.capitalize())  # Capitalize first letter
print(name.title())  # Title case
print(name.lower())  # Convert to lowercase
print(name.replace("A", "@"))  # Replace 'A' with '@'
print(name.count("a"))  # Count occurrences of 'a'
print(len(name))  # Length of the string
print(name.strip())  # Remove leading and trailing whitespace

print(name.upper().replace("A", "*"))  # Uppercase and replace 'A' with '*' COMBINE METHODS


# Intermediate Practice

full_name = "Aryan Dnyandev Bhagwat"

print(full_name[0]) # It will print the first character of full_name
print(full_name[-1]) # It will print the last character of full_name
print(full_name.upper()) # It will print full_name in uppercase
print(full_name.title()) # It will print full_name in title case
print(len(full_name)) # It will print the length of full_name

string = str(input("Enter a string: "))  # Input from user
print(string[::-1]) # Reverse the string
print(len(string))  # Total number of characters in the string
print(len(string.split())) # Count number of words in the string
print(string.replace("bad", "good"))  # Replace 'bad' with 'good'


# Bonus Challenge : Bulid a username generator
print("Welcome to the username generator!")

first_name = str(input("Enter your first name: "))
last_name = str(input("Enter your last name: "))
fav_num = int(input("Enter your favorite number: "))

print("username: " + first_name[:3] + last_name[-3:] + str(fav_num))  # Create username