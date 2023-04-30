from typing import Dict

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
}


def capp(men, qur, dime, nik, penny, resources):
    cappuccino = (MENU['cappuccino'])
    cost_cap = (cappuccino['cost'])
    ing_cap = (cappuccino['ingredients'])

    if resources['water'] < 250:
        print("Sorry there is not enough water.")
    elif resources['milk'] < 100:
        print("Sorry there is not enough milk.")
    elif resources['coffee'] < 24:
        print("Sorry there is not enough coffee")
    else:
        resources['milk'] -= 100
        resources['coffee'] -= 24
        total_cost = (qur * 0.25) + (dime * 0.10) + (nik * 0.05) + (penny * 0.01)
        resources['water'] -= 250
        if total_cost >= cost_cap:
            change = round(total_cost - cost_cap, 2)
            print(f"Here is {change} in change.")
            print("Here is your cappuccino, Enjoy!")
        else:
            print("Sorry that's not enough money. Money Refunded")

def exp(men, qur, dime, nik, penny, resources):
    espresso = (MENU['espresso'])
    ing_esp = (espresso['ingredients'])
    cost_esp = (espresso['cost'])

    if resources['water'] < 50:
        print("Sorry there is not enough water.")
    elif resources['coffee'] < 18:
        print("Sorry there is not enough coffee")
    else:
        resources['water'] -= 50
        resources['coffee'] -= 18
        total_cost = (qur * 0.25) + (dime * 0.10) + (nik * 0.05) + (penny * 0.01)
        if total_cost >= cost_esp:
            change = round(total_cost - cost_esp, 2)
            print(f"Here is {change} in change.")
            print("Here is your espresso, Enjoy!")
        else:
            print("Sorry that's not enough money. Money Refunded")

def lat(men, resources):
    latte = (men['latte'])
    ing_latte = (latte['ingredients'])
    cost_latte = (latte['cost'])

    if resources['water'] < 200:
        print("Sorry there is not enough water.")
    elif resources['milk'] < 150:
        print("Sorry there is not enough milk.")
    elif resources['coffee'] < 24:
        print("Sorry there is not enough coffee")
    else:
        print("Please insert coins.")
        qur = int(input("How many quarters?"))
        dime = int(input("How many dimes?"))
        nik = int(input("How many nickles?"))
        penny = int(input("How many pennies?"))

        resources['water'] -= 200
        resources['milk'] -= 150
        resources['coffee'] -= 25
        total_cost = (qur * 0.25) + (dime * 0.10) + (nik * 0.05) + (penny * 0.01)
        if total_cost >= cost_latte:
            change = round(total_cost - cost_latte, 2)
            print(f"Here is {change} in change.")
            print("Here is your latte, Enjoy!")
        else:
            print("Sorry that's not enough money. Money Refunded")

continue_game = True
while continue_game == True:

    order = input("What would you like? (espresso/latte/cappuccino)")
    if order == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
    elif order == 'latte':
        lat(MENU, resources)

    elif order == 'espresso':
        print("Please insert coins.")
        qur = int(input("How many quarters?"))
        dime = int(input("How many dimes?"))
        nik = int(input("How many nickles?"))
        penny = int(input("How many pennies?"))
        exp(MENU, qur, dime, nik, penny, resources)
    elif order == 'cappuccino':
        print("Please insert coins.")
        qur = int(input("How many quarters?"))
        dime = int(input("How many dimes?"))
        nik = int(input("How many nickles?"))
        penny = int(input("How many pennies?"))
        capp(MENU, qur, dime, nik, penny, resources)
    elif order == 'off':
        print("Thank you for visiting!")
        continue_game = False
    else:
        print("You entered wrong input.")
