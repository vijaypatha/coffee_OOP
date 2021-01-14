# TODO: From Module Import Classes
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO: Create Objects by initiating the Imported Classes
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    # TODO: Get Options and prompt user for input
    options = menu.get_items()
    user_choice = input(f"What would you like? {options} ")

    if user_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif user_choice == 'off':
        is_on = False
    else:
        # TODO:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)




