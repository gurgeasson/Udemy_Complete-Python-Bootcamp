print("Welcome to Python Pizza Deliveries!")

size_valid_options = ["6\"", "1'", "2'", "6", "1", "2", "6 inch", "1 foot", "2 feet", "6 inch"]
yes_valid_options = ["y", "yes", "sure", "aha", "maybe"]
no_valid_options = ["n", "no"]
size = False
pepperoni = False
cheese = False
total = 15.00
one_foot_difference = 5.00
two_feet_difference = 10.00
pepperoni_6inch_price = 2.00
pepperoni_big_price = 3.00
cheese_price = 1.00

while size not in size_valid_options:
    if size == False:
        size = input("What size pizza would you like? 6\", 1', 2': ").lower()
    else:
        size = input("Please check your answer. What size pizza would you like? Valid options are: 6\", 1', 2' ").lower()
while pepperoni not in yes_valid_options and pepperoni not in no_valid_options:
    if pepperoni == False:
        pepperoni = input("Would you like pepperoni on your pizza? Y or N: ").lower()
    else:
        pepperoni = input("Please check your answer. Would you like pepperoni on your pizza? Valid options are: Y or N: ").lower()
while cheese not in yes_valid_options and cheese not in no_valid_options:
    if cheese == False:
        cheese = input("Would you like extra cheese? Y or N: ").lower()
    else:
        cheese = input("Please check your answer. Would you like extra cheese? Valid options are: Y or N: ").lower()

match size[0]:
    case "6":
        print(f"6\" pizza: £{total}")
    case "1":
        total += one_foot_difference
        print(f"1' pizza: £{total + one_foot_difference}")
    case "2":
        total += two_feet_difference
        print(f"2' pizza: £{total + two_feet_difference}")
    case _:
        print("something's wrong with size")
        exit

if pepperoni in yes_valid_options:
    if size[0] == "6":
        total += pepperoni_6inch_price
        print(f"pepperoni: £{pepperoni_6inch_price}")
    else:
        total += pepperoni_big_price
        print(f"pepperoni: £{pepperoni_big_price}")
elif pepperoni in no_valid_options:
    pass
else:
    print("something is wrong with pepperoni")

if cheese in yes_valid_options:
    total += cheese_price
    print(f"cheese: £{cheese_price}")
elif cheese in no_valid_options:
    pass
else:
    print("something is wrong with cheese")

print(f"the total is: £{total}")

