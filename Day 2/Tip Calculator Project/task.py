print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_as_percentage = tip / 100
total_tip_amount = bill * tip_as_percentage
total_amount = bill + total_tip_amount
each_person_amount = total_amount / people
print(f"Each person should pay : {round(each_person_amount,2)}" )


