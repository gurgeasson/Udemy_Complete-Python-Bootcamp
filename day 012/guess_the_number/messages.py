WELCOME = "Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100."
CHOOSE_DIFFICULTY = "Choose a difficulty. Type 'easy' or 'hard': "
MAKE_GUESS = "Make a guess: "
GUESS_HIGH = "Too high."
GUESS_LOW = "Too low."
GUESS_CORRECT = "That is correct!"
GUESS_AGAIN = "Guess again."
LOST = "Sorry, you run out of guesses. You lost"
WON = "Yay, You won!"

def tell_number_of_attempts(NUMBER_OF_ATTEMPTS, number_of_attempts):
    """function to assembele number of attempts message"""
    if number_of_attempts in NUMBER_OF_ATTEMPTS:
        if number_of_attempts > 1:
            return f"You have {number_of_attempts} attempts to guess the number."
        else:
            return f"You have {number_of_attempts} attempt to guess the number."
    else:
        if number_of_attempts > 1:
            return f"You have {number_of_attempts} remaining attempts to guess the number."
        else:
            return f"You have {number_of_attempts} remaining attempt to guess the number."

LOGO = r"""
    _   __                __                 ______                     _                ______                   
   / | / /_  ______ ___  / /_  ___  _____   / ____/_  _____  __________(_)___  ____ _   / ____/___ _____ ___  ___ 
  /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/  / / __/ / / / _ \/ ___/ ___/ / __ \/ __ `/  / / __/ __ `/ __ `__ \/ _ \
 / /|  / /_/ / / / / / / /_/ /  __/ /     / /_/ / /_/ /  __(__  |__  ) / / / / /_/ /  / /_/ / /_/ / / / / / /  __/
/_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/      \____/\__,_/\___/____/____/_/_/ /_/\__, /   \____/\__,_/_/ /_/ /_/\___/ 
                                                                            /____/                                
"""
# ascii from https://patorjk.com/software/taag/
