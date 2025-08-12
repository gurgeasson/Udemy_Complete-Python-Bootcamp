import random

list_of_friends = ["Flaky", "Cuddles", "Nutty", "Petunia", "Lumpy", "Disco Bear", "Cub", "Sniffles", "Lammy", "Russell", "Pop"]

unlucky_soul = list_of_friends[random.randint(0, len(list_of_friends) - 1)]
print(unlucky_soul)

print(random.choice(list_of_friends))
