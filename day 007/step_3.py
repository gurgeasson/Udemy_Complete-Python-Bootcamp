import random
import hangman_ascii

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for letter in chosen_word:
    placeholder = placeholder + "_"
print(placeholder)

correct_guesses = []
wrong_guesses = []

in_game = True

while in_game:
    display = ""
    guess = input("Guess a letter: ").lower()
    if guess not in letters:
        print(f"{guess} is not a valid option")
        continue
    if guess in correct_guesses or guess in wrong_guesses:
        print(f"you already guessed '{guess}'")
        continue
    if guess in chosen_word:
        correct_guesses.append(guess)
    else:
        wrong_guesses.append(guess)
    
    for letter in chosen_word:
        if letter == guess:
            display += letter
        elif letter in correct_guesses:
            display += letter
        else:
            display += "_"
    print(display)
    print(hangman_ascii.ascii_hangman_steps[len(wrong_guesses)])

    if "_" not in display:
        in_game = False
        print(f"You Won!\n {hangman_ascii.ascii_hangman_steps[7]}")
    if len(wrong_guesses) > 5:
        in_game = False
        print("You Lost!")


print("Game Over")
