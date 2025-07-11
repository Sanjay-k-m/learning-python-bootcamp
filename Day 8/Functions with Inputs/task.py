def greet():
    print("Hello" )
    print("dude")
    print("How are you")


greet()

def greet_with_name(name):
    print("Hello",name)
    print(f"How are you {name}.")

greet_with_name("sanju")

def gree_with_name_with_default_value(name="sanjuuuu"):
    print(f"hello {name}")

gree_with_name_with_default_value()