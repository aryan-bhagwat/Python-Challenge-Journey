# Day 12 Challenge: Print all keyword arguments using **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage
print_info(name="Aryan", role="Data Scientist", experience="Intern")
