import art

print(art.logo)
# TODO-1: Ask the user for input
def compare(bids):
    winner=""
    highest_bid=0
    for bidder in bids:
        bid_amount=bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            bid_amount = bidder
            winner=bidder



    print(f"The winner is {winner} with a bid of ${highest_bid}")
# TODO-2: Save data into dictionary {name: price}
user_name = input("Please enter your name:")
user_bid = int(input("Please enter the bid:$"))

bids={}
# TODO-3: Whether if new bids need to be added
should_continue=input("Are there any other bids? if yes then type 'yes' or type 'no'\n")
continue_bids=True
while continue_bids:
    user_name = input("Please enter your name:")
    user_bid = int(input("Please enter the bid:$"))
    bids[user_name] = user_bid
    should_continue = input("Are there any other bids? if yes then type 'yes' or type 'no'\n")
    if should_continue == "no" :
        continue_bids=False
        compare(bids)
    elif should_continue == "yes":
        print("\n" * 50)
# TODO-4: Compare bids in dictionary

