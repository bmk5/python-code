from data import MENU, resources

MONEY = 0.0
DRINKS = ["espresso", "latte", "cappuccino"]


def print_report():
    """This method prints the current resources available to the console"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${MONEY}")


def are_resources_present(drink):
    """Returns true if the ingredients required to make the given drink are available, otherwise, False"""
    ingredients = MENU[drink]["ingredients"]
    for ingredient in ingredients:
        needed_amount = ingredients[ingredient]
        available = resources[ingredient]
        if needed_amount > available:
            print(f"Sorry there is not enough {ingredient}.")
            return False

    return True


def add_sale(cost):
    """Increments the money in the machine"""
    global MONEY
    MONEY += cost


def update_resources(drink):
    """This method subtracts the amount of ingredients used in making a drink from the resources"""
    ingredients = MENU[drink]["ingredients"]
    for ingredient in ingredients:
        amount = ingredients[ingredient]
        resources[ingredient] -= amount


def get_money():
    """Prompts the user to insert coins and returns the total value of the coins"""
    print("Please insert coins")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    return (pennies * 0.01) + (nickels * 0.05) + (dimes * 0.1) + (quarters[0] * 0.25)


def game():
    """Instantiates the coffee machine. Returns True to shut down the coffee machine, otherwise False"""
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if drink in DRINKS:
        if are_resources_present(drink):
            total = get_money()
            cost = MENU[drink]["cost"]

            if total >= cost:
                change = round(total - cost, 2)
                add_sale(cost)
                update_resources(drink)

                if change > 0:
                    print(f"Here is ${change} in change")
                print(f"Here is your {drink}. Enjoy!")

            else:
                print("Sorry that's not enough money. Money refunded.")

        return False

    elif drink == "report":
        print_report()
        return False

    elif drink == "off":
        return True

    else:
        print("You have entered an invalid choice, please try again.")
        return False


machine_off = False
while not machine_off:
    machine_off = game()
