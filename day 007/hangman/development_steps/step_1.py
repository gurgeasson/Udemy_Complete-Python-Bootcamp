import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - choose random word from word_list and place in chosen_word, then print it

# TODO-2 - Ask user to guess a letter and assign answer to variable guess. Make guess lower case

# TODO-3 - Check if guess is in chosen_word. If true, print 'good guess', if false print 'wrong'

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Good guess")
    else:
        print("Wrong")

# while True:
#     guess = input("guess a letter: ").lower()
#     if guess in chosen_word:
#         print("Good guess")
#     else:
#         print("Wrong")
