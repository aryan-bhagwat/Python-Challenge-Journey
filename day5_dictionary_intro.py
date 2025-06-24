# Day 5 Challenge: Store user info using a dictionary

user = {}

# Collect user details
user['name'] = input("Enter your name: ")
user['age'] = input("Enter your age: ")
user['city'] = input("Enter your city: ")
user['language'] = input("Favorite programming language: ")

# Print user profile
print("\n👤 User Profile:")
for key, value in user.items():
    print(f"{key.capitalize()}: {value}")
