import random
import sys
import os
import art
import game_data

score = 0

if len(game_data.data) == 1:
    sys.exit("error: not enough data in game data bank")

def check_decision(player_choice, followers_a, followers_b):
    """take player coice and the two prospect's number of followers and return if player is right as a boolean"""
    if player_choice == "a":
        if followers_a > followers_b:
            return True
        elif followers_a == followers_b:
            return True
        else:
            return False
    else:
        if followers_b > followers_a:
            return True
        elif followers_b == followers_a:
            return True
        else:
            return False

def pick_random_prospect_from_list_of_dictionaries(data, a):
    """takes a list and an item that it can't take from that list to avoid picking same item again, and returns an item from the list"""
    prospect = {}
    if a == {}:
        prospect = random.choice(data)
    else:
        while prospect == {} or prospect == a:
            prospect = random.choice(data)        
    return prospect

while True:
    prospect_a = pick_random_prospect_from_list_of_dictionaries(game_data.data, {})
    prospect_b = pick_random_prospect_from_list_of_dictionaries(game_data.data, prospect_a)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(art.logo)
    print(f"Compare A: {prospect_a['name']}, a {prospect_a['description']}, from {prospect_a['country']}.")
    print(art.vs)
    print(f"Against B: {prospect_b['name']}, a {prospect_b['description']}, from {prospect_b['country']}.")
    valid_input = False
    while not valid_input:
        player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if player_choice in ["a", "b"]:
            valid_input = True
    if check_decision(player_choice, prospect_a["follower_count"], prospect_b["follower_count"]):
        score += 1
        print(f"You're right! Current score: {score}")
        input("to continue, press 'enter'")
    else:
        break
print(f"Sorry, that's wrong. Final score: {score}")
