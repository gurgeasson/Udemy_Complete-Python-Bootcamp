letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def shift_letter_by(letter, shift):
    return letters[letters.index(letter) + shift]

print(shift_letter_by(input("give us a letter   "), 1))

message = input("give us message   ")
shift = 1

for letter in 
