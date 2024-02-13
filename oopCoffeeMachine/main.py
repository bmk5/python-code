from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def game(menu, coffee_machine, balance):
    items = menu.get_items()[:-1]
    drink = input(f"What would you like? ({items}): ").lower()

    if drink == 'report':
        coffee_machine.report()
        balance.report()
        return True

    if drink == 'off':
        return False

    item = menu.find_drink(drink)

    if item is None:
        return True

    if coffee_machine.is_resource_sufficient(item) and balance.make_payment(item.cost):
        coffee_machine.make_coffee(item)

    return True


menu = Menu()
machine = CoffeeMaker()
money = MoneyMachine()
machine_on = True

while machine_on:
    machine_on = game(menu, machine, money)
