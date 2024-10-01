print("Welcome to the auction prpogram.")
def find_highest_bidder(bidding_dictionary):
    winner =  ""
    highest_bid=0
    max(bidding_dictionary)
    for bidder in bidding_dictionary:
        bid_amt=bidding_dictionary[bidder]
        if bid_amt > highest_bid:
            highest_bid=bid_amt
            winner = bidder
            
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    
    
lib={}
continue_bidding = True
while continue_bidding:
    name=input("What is your name?:")
    bid_amt=int(input("What's your bid?:"))
    lib[name]=bid_amt
    other_bidders=input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if other_bidders == "no":
        continue_bidding=False
        find_highest_bidder(lib)
    elif other_bidders == "yes":
        print("\n"*200)


    
    