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


def check_resources(drink):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if resources[ingredient] < amount:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True


def process_coin():
    print("Please insert coins.")
    quarter_input = int(input("How many quarters?")) * .25
    dime_input = int(input("How many dimes?")) * .1
    nickle_input = int(input("How many nickles?")) * .05
    penny_input = int(input("How many pennies?")) * .01
    return quarter_input + dime_input + nickle_input + penny_input


def make_coffee(drink_name):
    for ingredient, amount in MENU[drink_name]["ingredients"].items():
        resources[ingredient] -= amount
    global profit
    profit += MENU[drink_name]["cost"]
    print(f"Here is your {drink_name} ☕ Enjoy!")


profit = 0
machine_running = True
while machine_running:

    user_input = input("What would you like? (espresso/latte/cappuccino):").lower()

    acceptable_inputs = ["espresso", "latte", "cappuccino", "off", "report"]

    if user_input not in acceptable_inputs:
        print("Wrong input. Please enter correct input")

    if user_input == "off":
        print("Turning off machine. Good Bye")
        machine_running = False

    elif user_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    elif user_input in ["espresso", "latte", "cappuccino"]:
        drink = user_input
        if check_resources(drink):
            payment = process_coin()
            if payment > MENU[drink]["cost"]:
                change = round(payment - MENU[drink]["cost"], 2)
                print(f"Here is ${change} in change.")
                make_coffee(drink)
            else:
                print("Sorry. Not enough money. Money Refunded")

