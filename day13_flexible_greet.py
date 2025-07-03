# Day 13 Challenge: Combine default param, *args, and **kwargs
def greet(greeting="Hello", *names, **details):
    for name in names:
        print(f"{greeting}, {name}!")
    for key, value in details.items():
        print(f"{key}: {value}")

# Example usage
greet("Hi", "Aryan", "Dev", role="Data Scientist", level="Intern")
