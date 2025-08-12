bill = float(input("Welcome to the tip calculator!\nWhat was the total bill?\n£"))
tip_percentage = int(input("How much tip would you like to give? Accepts percentage withouth\n%"))
tip = bill * tip_percentage / 100
bill_with_tip = bill + tip
number_of_people = int(input("How many people to split the bill?\n"))
single_person_total = round(bill_with_tip / number_of_people, 2)
print(f"Each person should pay: £{single_person_total}")
