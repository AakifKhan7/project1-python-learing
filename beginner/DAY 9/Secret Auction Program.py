logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bids = {}
auction_over = False

def find_highest_biding(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the highest bid ${highest_bid}")

while auction_over == False:
    name = input("Enter Your name : ")
    Bid_price = int(input("Enter Your Bid price : $"))
    other_people = input("type 'yes' if there is any other player otherwise 'no'\n").lower()
    bids[name] = Bid_price

    if other_people == "no":
        auction_over = True
        find_highest_biding(bids)