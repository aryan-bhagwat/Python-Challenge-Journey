# Day 4 Challenge: Basic List Operations

# Create an empty list
fruits = []

# Ask user for 3 favorite fruits
for i in range(3):
    fruit = input(f"Enter favorite fruit #{i+1}: ")
    fruits.append(fruit)

# Display results
print("\nYour fruit list:")
print(fruits)
print(f"First fruit: {fruits[0]}")
print(f"Sorted list: {sorted(fruits)}")
