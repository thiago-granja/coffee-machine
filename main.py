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
    "water": 10000,
    "milk": 3000,
    "coffee": 1000,
    "money": 30,
}


def report():
    """Returns a report on the machine's current resources."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def beverage_available(beverage):
    """Checks availability of a beverage. Returns True if available, False if not."""
    if beverage == 'espresso':
        espresso_water = MENU['espresso']['ingredients']['water']
        espresso_coffee = MENU['espresso']['ingredients']['coffee']
        if espresso_water <= resources['water'] and espresso_coffee <= resources['coffee']:
            return True
        else:
            return False
    if beverage == 'latte':
        latte_water = MENU['latte']['ingredients']['water']
        latte_milk = MENU['latte']['ingredients']['milk']
        latte_coffee = MENU['latte']['ingredients']['coffee']
        if latte_water <= resources['water'] and latte_milk <= resources['milk'] and latte_coffee <= \
                      resources['coffee']:
            return True
        else:
            return False
    if beverage == 'cappuccino':
        cappuccino_water = MENU['cappuccino']['ingredients']['water']
        cappuccino_milk = MENU['cappuccino']['ingredients']['milk']
        cappuccino_coffee = MENU['cappuccino']['ingredients']['coffee']
        if cappuccino_water <= resources['water'] and cappuccino_milk <= resources[
        'milk'] and cappuccino_coffee <= resources['coffee']:
            return True
        else:
            return False


def turn_on():
    turnoff = False
    while not turnoff:
        ccost = 0
        cwater = 0
        ccoffee = 0
        cmilk = 0
        money_inserted = 0
        espresso_available = beverage_available('espresso')
        latte_available = beverage_available('latte')
        cappuccino_available = beverage_available('cappuccino')

        choice_text = "What would you like? ( "
        if espresso_available:
            choice_text += "[espresso] "
        if latte_available:
            choice_text += "[latte] "
        if cappuccino_available:
            choice_text += "[cappuccino] "
        choice_text += ") "
        if len(choice_text) < 26:
            choice_text = "Sorry, all items are unavailable. Please contact XYZ (the HR guy). "

        choice = input(f"{choice_text}")
        if choice == 'espresso' and not beverage_available('espresso') or choice == 'latte' and not beverage_available('latte') or choice == 'cappuccino' and not beverage_available('cappuccino'):
            print ("Sorry, this item is unavailable.")
        elif choice == 'report':
            report()
        elif choice == 'off':
            turnoff = True
        elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
            cwater = MENU[choice]['ingredients']['water']
            ccoffee = MENU[choice]['ingredients']['coffee']
            ccost = MENU[choice]['cost']
            if choice != 'espresso':
                cmilk = MENU[choice]['ingredients']['milk']
            print("Please insert coins.")
            quarters = input("How many quarters? ")
            if quarters.isnumeric():
                money_inserted += float(quarters) * .25
            dimes = input("How many dimes? ")
            if dimes.isnumeric():
                money_inserted += float(dimes) * .1
            nickels = input("How many nickels? ")
            if nickels.isnumeric():
                money_inserted += float(nickels) * .05
            pennies = input("How many pennies? ")
            if pennies.isnumeric():
                money_inserted += float(pennies) * .01

            change = round(money_inserted - ccost, 2)
            if change >= -.1 and change <= resources['money']:
                if change > 0:
                    print(f"Here's ${change} in change. Enjoy your {choice}!")
                if change == 0:
                    print(f"No change needed. Enjoy your {choice}!")
                if change < 0:
                    print(f"You inserted ${change*(-1)} less than required. Don't worry, the rest is on us! :)")
                    ccost += change
                resources['money'] += ccost
                resources['water'] -= cwater
                resources['milk'] -= cmilk
                resources['coffee'] -= ccoffee

            elif change > resources['money']:
                print("Sorry, we're short on change. Money refunded.")

            else:
                print ("Sorry, that's not enough money. Money refunded.")

        else:
            print ("Invalid input.")

turn_on()