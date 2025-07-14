
try:
    age = int(input("How old are you?"))
except  ValueError:
    print("The value must be a valid number. Please Try again with a numberical number")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")

