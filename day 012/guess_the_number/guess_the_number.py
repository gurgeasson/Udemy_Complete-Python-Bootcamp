from random import randint
import messages
import functions

THE_NUMBER = randint(1, 100)
POSSIBLE_NUMBER_OF_ATTEMPTS = [5, 10]
number_of_attempts = 0
lost = True

print(messages.LOGO)
print(messages.WELCOME)
number_of_attempts = functions.set_difficulty(input(messages.CHOOSE_DIFFICULTY).lower(), POSSIBLE_NUMBER_OF_ATTEMPTS)

while number_of_attempts > 0:
    print(messages.tell_number_of_attempts(POSSIBLE_NUMBER_OF_ATTEMPTS, number_of_attempts))
    round_outcome = functions.evaluate_guess(THE_NUMBER, int(input(messages.MAKE_GUESS)))
    if round_outcome == 0:
        print(messages.GUESS_CORRECT)
        lost = False
        break
    elif round_outcome == -1:
        print(messages.GUESS_LOW)
        number_of_attempts -= 1
    elif round_outcome == 1:
        print(messages.GUESS_HIGH)
        number_of_attempts -= 2
if lost:
    print(messages.LOST)
elif not lost:
    print(messages.WON)
