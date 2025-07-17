MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

COIN_VALUES = {"quarters" : 0.25,"dimes":0.10,"nickles":0.05,"pennies":0.01}

VALID_USER_INPUT = {"1":"espresso","2":"latte","3":"cappuccino","off":"off","report":"report"}

# to take user input and validate user input
def user_input_prompt():
    user_input =  input("What would you like? \n 1. espresso\n 2. latte \n 3. cappuccino \n Your Choice : ").lower()
    if user_input not in VALID_USER_INPUT:
        print("invalid choice, try with valid input.")
        return user_input_prompt()
    else:
        return VALID_USER_INPUT[user_input]


# to get details about resource data
def resource_report():
    for resource in resources:
        print(f"{resource.capitalize()} : {resources[resource]}")
    input(f"Press Enter to continue...")
    print("\n" * 30)

#cheking resource is enough for selected drink if it's not enough then call user input prompt function
def check_resource_sufficient(selected_drink, resources, MENU):
    for ingredient in MENU[selected_drink]["ingredients"]:
        while not resources[ingredient] >= MENU[selected_drink]["ingredients"][ingredient]:
            input(f"Sorry, there is not enough {ingredient.capitalize()}. Press Enter to continue...")
            print("\n" * 30)
            user_input_prompt()

# to find total money of given coins
def process_coin():
    print("Please insert coins. \n")
    quarters = int(input("How many quarters : "))
    dimes = int(input("How many dimes : "))
    nickles = int(input("How many nickel : "))
    pennies = int(input("How many pennies : "))
    total_coins = COIN_VALUES["quarters"] * quarters + COIN_VALUES["dimes"] * dimes + COIN_VALUES["nickles"] * nickles + COIN_VALUES["pennies"] * pennies
    return total_coins

# if transaction is success then reduce ingredient
def reduce_ingredients(selected_drink, resources, MENU):
    for ingredient in MENU[selected_drink]["ingredients"]:
        resources[ingredient] -= MENU[selected_drink]["ingredients"][ingredient]
# if enough money then transaction become  success and make changes in resource otherwise run input promp again
def check_transaction(total_coin,selected_drink,MENU,resources):
    if total_coin >= MENU[selected_drink]["cost"]:
        balance = MENU[selected_drink]["cost"] - total_coin
        if balance != 0:
            print(f"Here is ${balance} in change")
        resources["money"] += MENU[selected_drink]["cost"]
        input(f"Here is your {selected_drink} ☕. Enjoy! . Press Enter to continue...")
        reduce_ingredients(selected_drink, resources, MENU)
        print("\n" * 30)
        user_input_prompt()
    else :
        input("Sorry that's not enough money. Money refunded. . Press Enter to continue...")
        print("\n" * 30)
        user_input_prompt()


# resource_report()
# print(user_input_prompt())
# check_resource_sufficient("latte",resources,MENU)
# print(check_resource_sufficient("espresso",resources = resources,MENU=MENU))
# print(process_coin())

while_machine_on = True

while while_machine_on:
    selected_drink = user_input_prompt()
    if selected_drink == "off":
        break
    elif selected_drink == "report":
        resource_report()
        continue
    check_resource_sufficient(selected_drink,resources,MENU)
    total_coin =  process_coin()
    check_transaction(total_coin,selected_drink,MENU,resources)




