# Day 19 : Advanced Function Techniques in Python

## 1. *args – Variable Number of Positional Arguments
def add_all(*args):
    return sum(args)

print(add_all(2,4,6,7))


# 2. **kwargs – Variable Number of Keyword Arguments
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_details(name="Aryan", age=20, city="Navi Mumbai")