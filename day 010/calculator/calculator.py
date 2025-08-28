import art
import calc_operations

continue_switch = True

operations = {
    "+": calc_operations.add,
    "-": calc_operations.substract,
    "*": calc_operations.multiply,
    "/": calc_operations.divide
}

print(art.logo)

first_number = int(input("first numer: "))
for symbol in operations:
    print(symbol)
operation = input("what operation?: ")

while True:
    second_number = int(input("second number: "))    
    result = operations[operation](first_number, second_number)    
    print(f"{first_number} {operation} {second_number} = {result}")
    next_step = input("Type an operator (+ - * /) and press enter to continue, or type \"End\" to Stop ")
    if next_step == "End":
        break
    elif next_step in ["+", "-", "*", "/"]:
        operation = next_step
        first_number = result
        continue
    else:
        print("error")
        break