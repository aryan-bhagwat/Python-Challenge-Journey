# Day 9 Challenge: BMI Calculator using a function

def calculate_bmi(weight_kg, height_m):
    return round(weight_kg / (height_m ** 2), 2)

# User input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi}")
