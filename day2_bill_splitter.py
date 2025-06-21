# Day 2 Challenge: Simple Bill Splitter

# Get inputs from user
total_bill = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))

# Calculate share per person
share = total_bill / people

# Print result rounded to 2 decimal places
print(f"\nEach person should pay: ₹{round(share, 2)}")
