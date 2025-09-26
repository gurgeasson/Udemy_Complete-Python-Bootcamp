# resources
resources = {
    "water": {
        10000: "ml"
    },
    "milk": {
        2000: "ml"
    },
    "coffee": {
        1000: "g"
    }
}

# drinks
drinks = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18
        },
        "price": 5.5
        },
        "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "price": 8.0
        },
        "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "price": 7.5
        }
        }

# functions
def report_resources():
    print("reporting...")
    for item in resources:
        for amount in resources[item]:
            print(f"{item}: {amount} {resources[item][amount]}")

def check_resource_sufficient(drink):
    for ingredient in drinks[drink]["ingredients"]:
        if resources[ingredient] < drinks[drink]["ingredients"][ingredient]:
            break
        else:
            return True
    return False

def use_resources():
    pass

def serve_drink(drink):
    if check_resource_sufficient(drink):
        use_resources()
        print("yasss")
    else:
        print(f"insufficient resources for making {drink}")

while True:
    item_to_serve = input("What would you like? (espresso/latte/cappucciono): ").lower()
    match item_to_serve:
        case "espresso" | "e":
            serve_drink("espresso")
        case "latte" | "l":
            serve_drink("latte")
        case "cappuccino"| "c":
            serve_drink("cappuccino")
        case "off":
            serve_drink("powering down... OFF")
            break
        case "report":
            report_resources()
        case _:
            print(f"{item_to_serve} is not an item served here")
            continue

