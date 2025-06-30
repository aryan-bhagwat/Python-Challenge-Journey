# Day 11 Challenge: Sum any number of arguments using *args
def sum_numbers(*args):
    return sum(args)

# Example usage
print("Sum of 3, 5:", sum_numbers(3, 5))
print("Sum of 1, 2, 3, 4:", sum_numbers(1, 2, 3, 4))
