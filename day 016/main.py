from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    item_customer_input = input(f"What would you like? ({menu.get_items()}): ").lower()
    match item_customer_input:
        case "off":
            print("powering down... OFF")
            break
        case "report":
            coffee_maker.report()
            money_machine.report()
        case _:
            item = menu.find_drink(item_customer_input)
            if item == None:
                print(f"{item_customer_input} is not an item served here")
                continue
            else:
                if coffee_maker.is_resource_sufficient(item):
                    print(f"{item.name} costs £{item.cost:.2f}")
                    if money_machine.make_payment(item.cost):
                        coffee_maker.make_coffee(item)
                    else:
                        print("not enough money")
                else:
                    print("no luck mate, not enough resources")
