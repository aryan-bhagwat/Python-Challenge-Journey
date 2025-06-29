# Day 10 Challenge: Greet with default message if no name is given

def greet(name="Guest"):
    print(f"Hello, {name}!")

# Try it with and without input
user_name = input("Enter your name (or leave blank): ")
if user_name.strip() == "":
    greet()
else:
    greet(user_name)
