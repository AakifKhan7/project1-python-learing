from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
Coffee_Maker = CoffeeMaker()
menu = Menu()

is_on = True

Coffee_Maker.report()
money_machine.report()

Coffee_Maker.is_resource_sufficient()

while is_on:
    option = menu.get_items()
    choice = input(f"What would you like? ({option})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        Coffee_Maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if Coffee_Maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            Coffee_Maker.make_coffee(drink)