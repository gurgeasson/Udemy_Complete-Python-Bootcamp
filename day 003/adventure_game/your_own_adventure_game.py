import ascii_art

yes_answer = ["Yes", "yes", "Y", "y", "igen"]
no_answer = ["No", "no", "N", "n", "nem"]

print(ascii_art.intro)
# https://ascii.co.uk/art/wasp
print("Welcome to the wasp garden, try to escape the wasps\n")
while True:
    if input("You are poking a wasps nest in the picturesque wasp garden." \
    " Do you want to hang around to see what happens? Yes/No: ") in no_answer:
        print("Good Choice.")
    else:
        print("You're in the hospital being treated for 1K+ wasp stings.")
        success = False
        break
    if input("You're making a hasty exist, but on your way out you " \
    "notice a £50 note in the grass. Pick it up? Yes/No: ") in no_answer:
        print("I agree, better not stop.")
    else:
        print("Oh no, it's monopoly money and the wasps got you.")
        success = False
        break
    final_choice = input("Now at the gate of the Wasp Graden, you can make your " \
    "final escape... but you just remembered, that you left your towel at the far " \
    "corner of the garden. Do you go back? Yes/No/Maybe/Sit down and think: ")
    if  final_choice in no_answer:
        print("You're out of the garden, safe now. Enjoy this cake.")
        success = True
    elif final_choice in yes_answer:
        print("You're crazy man.")
        success = False
    elif final_choice == "Maybe":
        print("Maybe the wasps got you.")
        success = False
    else:
        print("Too slow, you're dead.")
        success = False
    break
if success == False:
    print(ascii_art.you_loose)
else:
    print(ascii_art.you_win)
print("Game Over")
