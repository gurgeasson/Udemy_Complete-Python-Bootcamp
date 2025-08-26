bids = {}
name = ""
more_bids_switch = True
highest_bidder = "start_value"
print("Blind Bid Program")

while more_bids_switch:
    print("\n" *13)
    name = input("Type your name:\n")
    bids[name] = int(input("Type your bid:\n£"))
    if input("Are there more bidders? y/n:\n") == "y":
        more_bids_switch = True
    else:
        more_bids_switch = False

for bidder in bids:
    if highest_bidder == "start_value":
        highest_bidder = bidder
        continue
    if bids[highest_bidder] < bids[bidder]:
        highest_bidder = bidder
print("\n" *13)
print(f"The highest bidder is: {highest_bidder} with an amount of: {bids[highest_bidder]}")
