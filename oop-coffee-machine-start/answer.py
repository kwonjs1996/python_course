from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
turn_on = True
option = menu.get_items()
print(option)


while turn_on:
    choice = input(f"What do you want? {option}")
    if choice == "off":
        turn_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        # if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        if is_enough_ingredients and is_payment_successful:
            coffee_maker.make_coffee(drink)