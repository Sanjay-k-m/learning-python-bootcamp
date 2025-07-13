from calendar import firstweekday

import  art
def add(n1, n2):
    return n1 + n2
def divide(n1, n2):
    return n1 / n2
def multiply(n1, n2):
    return n1 * n2
def subtract(n1, n2):
    return n1 - n2

actions = {"+":add,"-":subtract,"/":divide,"*":multiply}

def print_operator():
    for operator in actions:
        print(operator)


game_over = False
number = 0
next_number = 0
first_stage = True
result = 0
while not game_over:
    selected_operator = ""
    if first_stage:
        print(art.logo)
        number = int(input("What is the first number ?"))
        print_operator()
        selected_operator =input("Select one operator from this... :")
        next_number = int(input("Enter the next number ..."))
        function = actions[selected_operator]
        result = function(number, next_number)
        print(f"{number} {selected_operator} {next_number} '=' {result}")
        first_stage = False
        userinput = input("Do you want to continue Yes or No ?")
        if userinput == "yes":
            game_over = True
    while game_over:
        print(art.logo)
        number = result

        next_number = int(input("Enter the next number ..."))
        print_operator()
        selected_operator = input("Select one operator from this... :")
        function = actions[selected_operator]
        print(f"{number} {selected_operator} {next_number} '=' {function(number, next_number)}")
        userinput = input("Do you want to continue Yes or No ?")
        if userinput == "yes":
            game_over = True
# Pick an operation: +
# What is the next number?: 45
# 40.0 + 45.0 = 85.0
# Type 'y' to continue calculating with 85.0, or type 'n' to start a new calculation:

