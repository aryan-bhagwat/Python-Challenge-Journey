# Day 16 : Dictionary Comprehension in Python
'''
names = ["Aryan", "Sana", "Ravi"]
marks = [85, 76, 92]

student_marks = {names[i]: marks[i] for i in range(len(names))}
print(student_marks)


nums = range(1, 6)
even_squares = {x: x**2 for x in nums if x % 2 == 0}
print(even_squares)  # Output: {2: 4, 4: 16}

word = "banana"
char_word = {char : word.count(char) for char in set(word)}
print(char_word)

names = ["Aryan", "Sana", "Ravi"]
marks = [85, 76, 92]

name_marks = {names[i] : marks[i] for i in range(len(names))}
print(name_marks)


# Create a dictionary with numbers as keys and their cubes as values from 1 to 5.
cube = {x : x**3 for x in range(1,6)}
print(cube)

# Build a dictionary of student names and their lengths.
stu_names = {x : len(x) for x in names}
print(stu_names)


# Convert a list of tuples to a dictionary:
data = [("a", 1), ("b", 2), ("c", 3)]

tuple_to_dic = {i[0] : i[1] for i in data}
print(tuple_to_dic)


# From a dictionary of student marks: Create a new dict with only students who passed (marks >= 60).

students = {"Aryan": 85, "Ravi": 45, "Sana": 76}

pass_students = {name : mark for name, mark in students.items() if mark >= 60}
print(pass_students)
'''

## Bonus Challenge : Grade Mapping System

students = ["Aryan", "Sana", "Ravi", "Manoj"]
marks = [85, 56, 92, 67]

stu_marks = {students[i] : "Excellent" if marks[i] >= 80 else "Good" if marks[i] >= 60 else "Fail"
             for i in range(len(students))}

print(stu_marks)