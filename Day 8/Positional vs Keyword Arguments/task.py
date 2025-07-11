# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")


def greet_with(name, location):
    print(f"hello {name}")
    print(f"what is it like in {location}")
# positional argument
greet_with("rathnamani","thalora")

# keyword argument
greet_with(location="thalora",name="sanjay")