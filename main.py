# Welcome to CodePad
# Edit, run, and push your Python code



def greet(name):
    return f"Hello, {name}!"

result = greet("World")
print(result)

import os

for key, value in os.environ.items():
    print(f"{key}={value}")