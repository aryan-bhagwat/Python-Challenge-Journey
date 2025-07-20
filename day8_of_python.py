# Day 8 : Dictionaries in Python (Key-Value Pairs)

''' Dictionaries are used to store data values in key:value pairs. 
They are unordered, changeable, and do not allow duplicates.
'''


## Basic Practice

person = {
    "name" : "Aryan",
    "age" : 20,
    "city" : "Mumbai",
    "is_student" : True
}

print(person["name"])  # Access value by key
print(person.get("age"))  # Access value using get method
print(person["city"]) # Access value by key
print(person.get("is_student"))  # Access value using get method
print(person.update({"city": "Navi Mumbai"}))  # Update value
person["skills"] = ["Python", "SQL"] # Add new key-value pair
print(person)  # Print the updated dictionary
print(person.keys())  # Print all keys
print(person.values())  # Print all values
print(person.items())  # Print all key-value pairs


## Intermediate Practice

stu_name = input("Enter your name: ")
stu_marks1 = int(input("Enter your marks in subject 1: "))
stu_marks2 = int(input("Enter your marks in subject 2: "))
stu_marks3 = int(input("Enter your marks in subject 3: "))

student = {
    "name" : stu_name,
    "marks" : {
        "subject1" : stu_marks1,
        "subject2" : stu_marks2,
        "subject3" : stu_marks3
    }
}
print(student)  # Print the student dictionary
Average = (stu_marks1 + stu_marks2 + stu_marks3) / 3
print(f"{stu_name}'s Average Score: {round(float(Average))}" )  # Calculate and print average score


## Bonus Challenge: Contact Book

contacts = {
    "Ravi": "9876543210",
    "Meena": "9876501234",
    "Aryan": "9988776655"
}

print(contacts)  # Print the All contacts
contacts["Tina"] = "9988776655"  # Add a new contact
contacts.pop("Meena")  # Remove a contact
print(contacts["Aryan"])  # Access a contact's number
print("Updated Contacts: ", contacts)  # Print the updated contacts