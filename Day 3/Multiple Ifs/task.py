print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    bill = 0
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
        bill +=5
    elif age <= 18:
        print("Please pay $7.")
        bill += 7
    else:
        print("Please pay $12.")
        bill +=12
    photo = input("Do you want photo ( charge 3$ ) y / n")
    if photo == "y":
        bill +=3
    print(f"you have to pay {bill} ")
else:
    print("Sorry you have to grow taller before you can ride.")
