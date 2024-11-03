import art

print(art.logo)
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

bids={}
should_continue=input("Are there any bids? if yes then type 'yes' or type 'no'\n") #asks for if there are any bids
continue_bids=True
while continue_bids:
    user_name = input("Please enter your name:")#asks the bidder's name
    user_bid = int(input("Please enter the bid:$"))#asks the bidder's bid 
    bids[user_name] = user_bid
    should_continue = input("Are there any other bids? if yes then type 'yes' or type 'no'\n")
    if should_continue == "no" :
        continue_bids=False
        compare(bids)#calls the function above to give the final result
    elif should_continue == "yes":
        print("\n" * 50)#prints fifty empty lines to hide the bids of other bidders

