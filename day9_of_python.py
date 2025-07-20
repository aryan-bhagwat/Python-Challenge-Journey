# Day 9 : if, elif, else – Decision Making in Python

## Basic Practice

age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")


## Intermidiate Practice : BMI Checker

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi}")

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Normal weight")
elif bmi >= 25 and bmi <= 29.9:
    print("Overweight")
elif bmi >= 30:
    print("Obese")


## Bonus Challenge : Tax Bracket Finder

income = float(input("Enter your annual income: "))

if income < 250000:
    print("No tax")
elif income >= 250000 and income < 500000:
    print(f"5% tax: {income * 0.05}")
elif income >=500000 and income < 1000000:
    print(f"20% tax: {income * 0.20}")
elif income >= 1000000:
    print(f"30% tax: {income * 0.30}")