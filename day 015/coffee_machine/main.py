# resources
resources = {
    "water": [10000, "ml"],
    "milk": [2000, "ml"],
    "coffee": [1000, "g"],
    "money": {"pound": 0,
            "fifty_p": 0,
            "twenty_p": 0,
            "ten_p": 0,
            "five_p": 0,
            "one_p": 0
            }
}

# drinks
DRINKS = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18
        },
        "price": 5.50
        },
        "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "price": 8.00
        },
        "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "price": 7.50
        }
        }

# functions
def report_resources():
    print("reporting...")
    for item in resources:
        if item == "money":
            print(f"{item}: {resources[item]}")
            print(f"TOTAL: £{count_coins(resources[item])}")
        else:
            print(f"{item}: {resources[item][0]} {resources[item][1]}")

def ask_for_coins(drink):
    print(f"{drink} costs £{DRINKS[drink]["price"]:.2f} Please insert coins")
    pound = int(input("How many pound coins(s)? "))
    fifty_p = int(input("How many 50p coin(s)? "))
    twenty_p = int(input("How many 20p coin(s)? "))
    ten_p = int(input("How many 10p coin(s)? "))
    five_p = int(input("How many 5p coin(s)? "))
    one_p = int(input("How many 1p coin(s)? "))
    return {"pound": pound,
            "fifty_p": fifty_p,
            "twenty_p": twenty_p,
            "ten_p": ten_p,
            "five_p": five_p,
            "one_p": one_p
            }

def count_coins(coins):
    return 1 * coins["pound"] + .5 * coins["fifty_p"] + .2 * coins["twenty_p"] + .1 * coins["ten_p"] + .05 * coins["five_p"] + .01 * coins["one_p"]

def take_coins(coins):
    for coin in coins:
        resources["money"][coin] = resources["money"][coin] + coins[coin]

def make_up_change(change):
    coins_in_change = {"pound": 1,
                       "fifty_p": .5,
                       "twenty_p": .2,
                       "ten_p": .1,
                       "five_p": .05,
                       "one_p": .01
                       }
    for coin in coins_in_change:
        amount_of_coin = change // coins_in_change[coin]
        if resources["money"][coin] == 0:
            pass
        elif resources["money"][coin] >= amount_of_coin:
            change = change - coins_in_change[coin] * amount_of_coin
            coins_in_change[coin] = amount_of_coin
        else:
            change = change - coins_in_change[coin] * resources["money"][coin]
            coins_in_change[coin] = resources["money"][coin]
    return coins_in_change

def check_resource_sufficient(drink):
    for ingredient in DRINKS[drink]["ingredients"]:
        if resources[ingredient][0] < DRINKS[drink]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def use_resources(drink):
    for ingredient in DRINKS[drink]["ingredients"]:
        resources[ingredient][0] = resources[ingredient][0] - DRINKS[drink]["ingredients"][ingredient]

def serve_drink(drink):
    if check_resource_sufficient(drink):
        coins_temporary_store = ask_for_coins(drink)
        total_sum_of_coins =  count_coins(coins_temporary_store)
        correct_fee = DRINKS[drink]["price"]
        change = total_sum_of_coins - correct_fee
        if change >= 0:
            use_resources(drink)
            take_coins(coins_temporary_store)
            coins_in_change = make_up_change(change)
            print(f"There you go, your {drink} served. luv ya\nAnd here's your change: £{change:.2f}\nAnd that is: {coins_in_change}")
        else:
            print(f"{drink} costs £{correct_fee:.2f} but you inserted £{total_sum_of_coins:.2f}... start again")
    else:
        pass

# loop
while True:
    item_to_serve = input("What would you like? (espresso/latte/cappucciono): ").lower()
    match item_to_serve:
        case "espresso" | "e":
            serve_drink("espresso")
        case "latte" | "l":
            serve_drink("latte")
        case "cappuccino" | "c":
            serve_drink("cappuccino")
        case "off":
            print("powering down... OFF")
            break
        case "report":
            report_resources()
        case _:
            print(f"{item_to_serve} is not an item served here")
            continue
