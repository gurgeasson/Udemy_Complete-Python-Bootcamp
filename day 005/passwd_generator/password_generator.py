#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

def pick_random_from_list(list_name, number_of_elements):
    passwd_shard = ""
    while number_of_elements > 0:
        number_of_elements -= 1        
        passwd_shard = passwd_shard + random.choice(list_name)
    return passwd_shard

print("Easy Level solution: " + pick_random_from_list(letters, nr_letters) + pick_random_from_list(numbers, nr_numbers) + pick_random_from_list(symbols, nr_symbols))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

def pick_random_from_list(list_name, number_of_elements):
    passwd_shard = []
    while number_of_elements > 0:
        number_of_elements -= 1        
        passwd_shard.append(random.choice(list_name))
    return passwd_shard

passwd_list = []
passwd_list.extend(pick_random_from_list(letters, nr_letters))
passwd_list.extend(pick_random_from_list(numbers, nr_numbers))
passwd_list.extend(pick_random_from_list(symbols, nr_symbols))
random.shuffle(passwd_list)
passwd = "".join(passwd_list)
print("hard Level solution: " + passwd)
