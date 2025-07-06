# Day 15 Challenge: Use map and lambda to square a list of numbers
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

print("Original:", numbers)
print("Squared:", squared)
