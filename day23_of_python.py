# Day 23 : JSON-Based CLI Student Database Manager

import json
import os

FILE_NAME = "students.json"

# Load data from file (if exists)
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# Save data to file
def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

# Add new student
def add_student(data):
    name = input("Enter student name: ")
    course = input("Enter course: ")
    score = int(input("Enter score: "))
    student = {"name": name, "course": course, "score": score}
    data.append(student)
    save_data(data)
    print(f"✅ Student {name} added successfully!")

# View all students
def view_students(data):
    if not data:
        print("No students found.")
        return
    for i, student in enumerate(data, start=1):
        print(f"{i}. {student['name']} - {student['course']} - {student['score']}")

# Search for a student
def search_student(data):
    keyword = input("Enter name to search: ").lower()
    results = [s for s in data if keyword in s['name'].lower()]
    if results:
        for s in results:
            print(f"{s['name']} - {s['course']} - {s['score']}")
    else:
        print("No matching student found.")

# Main program loop
def main():
    data = load_data()

    while True:
        print("\n--- Student Database Menu ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_student(data)
        elif choice == "2":
            view_students(data)
        elif choice == "3":
            search_student(data)
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

