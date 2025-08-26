letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

message = input("give us a message\n").lower()
shift = int(input("What is the shift?\n"))
cypher_switch = input("cypher or decypher?\n")
result = ""

def shift_letter_by(letter, shift):
    return letters[(letters.index(letter) + shift) % len(letters)]

if cypher_switch == "cypher":
    print("\nthe cyphered message:")
elif cypher_switch == "decypher":
    print("\nthe decyphered message:")
    shift = shift * -1

for letter in message:
    if letter in letters:
        result = result + shift_letter_by(letter, shift)
    else:
        result = result + letter

print(result)
