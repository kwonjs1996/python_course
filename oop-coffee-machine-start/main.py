from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
resource = coffee_maker.resources
turn = True
while turn:
    order = input(f"What do you want ? {menu.get_items()} ? ")
    if order == "report":
        money_machine.report()
        coffee_maker.report()
    elif order == "off":
        # 왜 return False ????안되는지?
        turn = False
    else:
        order = menu.find_drink(order)

        if coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)
