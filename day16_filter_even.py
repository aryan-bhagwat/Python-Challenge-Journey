# Day 16 Challenge: Use filter and lambda to extract even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))

print("Original:", numbers)
print("Even Numbers:", evens)
