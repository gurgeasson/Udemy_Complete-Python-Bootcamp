import random
import deck
player_hand = []
dealer_hand = []
all_dealt_cards = []
goal = 21
dealer_threshold = 17
number_of_decks = 1

def deal_card(amount):
    '''deal_card function takes the number of cards to deal as a paramater, and returns the list of dealt cards'''
    dealt_cards = []
    for n in range (amount):
        card_passed_awailibility_check = False
        while card_passed_awailibility_check == False:
            suit = random.choice(list(deck.standard_52_card_deck.keys()))
            card = random.choice(list(deck.standard_52_card_deck[suit].keys()))
            if all_dealt_cards.count({suit: card}) < number_of_decks:
                all_dealt_cards.append({suit: card})
                dealt_cards.append({suit: card})
                card_passed_awailibility_check = True
    return dealt_cards

def count_points(hand):
    '''count pontst for hand passed in the function as parameter. returns points'''
    points = 0
    ace_count = 0
    for round in hand:
        for card in round:
            for suit in card:
                if card[suit] == "A":
                    ace_count += 1
                else:
                    points += deck.standard_52_card_deck[suit][str(card[suit])]
    for n in range(ace_count):
        if points + deck.standard_52_card_deck[suit]["A"][0] > goal:
            points += deck.standard_52_card_deck[suit]["A"][1]
        else:
            points += deck.standard_52_card_deck[suit]["A"][0]
    return points


# greeting
print("A game of 21")

# 1) first round
player_hand.append(deal_card(2))
dealer_hand.append(deal_card(2))
print(player_hand)
print(count_points(player_hand))
# print(dealer_hand)
# print(count_points(dealer_hand))
print(list(dealer_hand[0][0].items())[0])


# 2) while True:
while True:
    if input("you wannna continue? y or n: ") == "n":
        break
    player_hand.append(deal_card(1))
    dealer_hand.append(deal_card(1))
    print(player_hand)
    print(count_points(player_hand))
    # print(dealer_hand)
    # print(count_points(dealer_hand))
    if count_points(player_hand) > goal:
        break

player_points = count_points(player_hand)
dealer_points = count_points(dealer_hand)
if dealer_points < dealer_threshold:
    dealer_hand.append(deal_card(1))
    dealer_points = count_points(dealer_hand)
print(f"{player_points} <---> {dealer_points}")
if player_points > goal:
    print("you lost")
elif dealer_points > goal:
    print("you won")
elif player_points == dealer_points:
    print("draw")
elif player_points < dealer_points:
    print("you lost")
else:
    print("you won")
