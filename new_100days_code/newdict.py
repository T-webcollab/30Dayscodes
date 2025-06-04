
Auction={}
end=False
def highest_bid(bidding):
    highest=0
    winner = ""
    for name in bidding:
        amount=bidding[name]
        if amount>highest:
            highest=amount
            winner=name
    print(f" {winner} is the winner of the auction")
        
while not end:
    
    name=input("Enter the name of bidder:")
    amount=int(input("enter the amount to be bid:"))
    Auction[name]=amount
    choice=input("do have more yes or no ").lower()
    if choice=="no":
        end=True
        highest_bid(Auction)