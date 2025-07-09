# Day 17 Challenge: Use zip() to pair elements of two lists
names = ["Aryan", "Dev", "Karan"]
roles = ["Analyst", "Developer", "Manager"]

paired = list(zip(names, roles))

print("Paired List:")
for name, role in paired:
    print(f"{name} - {role}")
