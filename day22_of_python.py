# Day 22 : Working with JSON in Python


## 1. Importing the json Module:
import json

## 2. Convert Python to JSON (Serialize):
import json

student = {
    "name": "Aryan",
    "course": "Python",
    "score": 95
}

json_data = json.dumps(student)
print(json_data)

## 3. Convert JSON to Python (Deserialize):
import json

json_data = '{"name": "Aryan", "course": "Python", "score": 95}'
student = json.loads(json_data)
print(student["name"])

## 4. Save JSON to File:
with open("student.json", "w") as f:
    json.dump(student, f)
    json.dumps(student, indent=4)        # Pretty print
    json.dumps(student, sort_keys=True)  # Sort by keys


## 5. Load JSON from File:
with open("student.json", "r") as f:
    data = json.load(f)
    print(data["grade"])


## Basic Practice :

# 1. Convert a dictionary of student info to a JSON string and print it.
# 2. Write that JSON string to a file.
import json

student = {
    "name": "Aryan",
    "course": "Python",
    "score": 95
}

stu_data = json.dumps(student)
print(stu_data)

with open("stu_data.json", "w") as f:
    json.dump(student, f)


## Intermediate Practice :

# 1. Create a Python list of 3 students (each student is a dictionary).
# 2. Save it to a file using json.dump.
# 3. Load the file back and print each student's name.
import json

student = [
    {
        "Name" : "Aryan",
        "Course" : "MCA",
        "Grade" : 'A'
    },
    {
        "Name" : "Mahesh",
        "Course" : "MCA",
        "Grade" : "B"
    },
    {
        "Name": "Charlie",
        "Course": "MBA",
        "Grade": "A-"
    }
]

with open("student.json", "w") as f:
    json.dump(student, f)

with open("student.json", "r") as file:
    data = json.load(file)

for student in data:
    print(student["Name"])


## Bonus Challenge: Student Data Manager

# 1. Ask user to enter name, course, and score.
# 2. Store each entry in a dictionary.
# 3. Append each student to a list.
# 4. Save the list to students.json.
# 5. On program start, if file exists, load previous data.
import json
import os 

students = []

if os.path.exists("students.json"):
    with open("students.json", "r") as f:
        try:
            loaded_data = json.load(f)
            if isinstance(loaded_data, list):
                students = loaded_data
            else:
                students = [loaded_data]
        except json.JSONDecodeError:
            students = []

for i in range(3):
    name = input("Enter your name: ")
    course = input("Enter your course: ")
    score = input("Enter your score: ")

    stu_dic = {
        "Name" : name,
        "Course" : course,
        "Score" : score
    }
    students.append(stu_dic)

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)