import random
import ascii_art

choices = [["rock", ascii_art.rock, ["rock", "r"]], ["paper", ascii_art.paper, ["paper", "p"]], ["scissors", ascii_art.scissors, ["scissors", "s"]]]
computer_choice = random.choice(choices)
player_choice = input("Type your choice - rock/paper/scissors: ").lower()
for val in choices:
    if player_choice in val[2]:
        player_choice = val
print(f"computer choose:\n{computer_choice[0]}\n{computer_choice[1]}")
print(f"player choose:\n{player_choice[0]}\n{player_choice[1]}")

if computer_choice[0] == player_choice[0]:
    print("draw")
elif computer_choice[0] == "rock" and player_choice[0] == "paper":
    print("you win")
elif computer_choice[0] == "paper" and player_choice[0] == "scissors":
    print("you win")
elif computer_choice[0] == "scissors" and player_choice[0] == "rock":
    print("you win")
else:
    print("you loose")