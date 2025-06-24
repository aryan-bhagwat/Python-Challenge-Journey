# Day 6 Challenge: Check if numbers in a list are even or odd

# Input: ask for 5 numbers
numbers = []

print("Enter 5 numbers:")
for i in range(5):
    num = int(input(f"Number {i+1}: "))
    numbers.append(num)

# Output: even or odd
print("\nResults:")
for n in numbers:
    result = "even" if n % 2 == 0 else "odd"
    print(f"{n} is {result}")
