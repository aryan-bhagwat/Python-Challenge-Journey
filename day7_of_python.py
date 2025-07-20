# Day 7 : Tuples and Sets in Python

## Tuples are immutable sequences, meaning they cannot be changed after creation.
## Sets are unordered collections of unique elements.


### Tuples : Basic Practice
cities = ("Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata")
print(cities[0]) # First city
print(cities[-1]) # Last city
print(cities[1:4]) # Slicing from 2nd to 4th city
# cities[1] = "Hyderabad"  # This will raise an error because tuples are immutable


### Sets : Basic Practice

numbers = {1, 2, 3, 4, 5}
numbers.add(6)  # Add a number to the set
print(numbers)  # Print the updated set of numbers
numbers.remove(3) # Remove a number from the set
print(numbers)  # Print the updated set of numbers
print(len(numbers))  # Length of the set
print(2 in numbers)  # Check if a number is in the set

### Bonus Challenge: Common Students

class_a = {"Aryan", "Ravi", "Meena", "Ali"}
class_b = {"Meena", "Tina", "Aryan"}

print("Common Students in Both Classes: ", class_a.intersection(class_b)) # Find common students
print("This is all students in both classes: ", class_a.union(class_b)) # Find all students in both classes
print("Students only in Class A: ", class_a.difference(class_b)) # Students only in Class A