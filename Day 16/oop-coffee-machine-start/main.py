from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_data = CoffeeMaker()
money_data = MoneyMachine()
menu = Menu()
print(menu.get_items())
machine_status = True
while machine_status:
    choice =  input(f"Prompt user by asking “What would you like? ({menu.get_items()}):").lower()
    if choice == "off":
        machine_status = False
    elif choice == "report":
        coffee_data.report()
        money_data.report()
    else:
        if  coffee_data.is_resource_sufficient(menu.find_drink(choice)) and money_data.make_payment(menu.find_drink(choice).cost):
            coffee_data.make_coffee(menu.find_drink(choice))


