import os

print("LOGO\n\n\n\n\n\n")

bid_dict = {}

while(True):
    name = input("Name: ")
    price = float(input("Price: "))
    
    bid_dict[name] = price
    
    bidders = input("Any oher bidders? (y/n):\n")
    
    if bidders == "y":
        os.system("cls")
    else:
        break

highest_bid = 0
highest = ''
for person in bid_dict:
    price_bid = bid_dict[person]
    
    if(price_bid > highest_bid):
        highest_bid = price_bid
        highest = f'{person} won bidding {highest_bid}'
    
print(highest)
    
    

    