import sys

def set_difficulty(difficulty, POSSIBLE_NUMBER_OF_ATTEMPTS):
    """returns the number of attemtps the payer starts with"""
    if difficulty in ["e", "easy"]:
        return POSSIBLE_NUMBER_OF_ATTEMPTS[1]
    elif difficulty in ["h", "hard"]:
        return POSSIBLE_NUMBER_OF_ATTEMPTS[0]
    else:
        sys.exit(f"error: can't interpret given input: '{difficulty}' as difficulty")

def evaluate_guess(THE_NUMBER, guess):
    """evaluates the gess against the number player needs to guess. returns -1 if too low, 0 if correct, 1 if too high"""
    if guess == THE_NUMBER:
        return 0
    elif guess < THE_NUMBER:
        return -1
    elif guess > THE_NUMBER:
        return 1
    else:
        sys.exit("error while evaluating guess")
