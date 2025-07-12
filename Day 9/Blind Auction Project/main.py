# TODO-1: Ask the user for input

game_over = False
import art
bid_data = {}
while not game_over:
    print(art.logo)
    name =input("\n Enter Your Name : \n")
    bid_amount = int(input("Enter the bid amount : \n "))
    bid_data[name] = bid_amount

    game_restart_status = input("Do you want to bid (yes or no) ?")
    if game_restart_status == "yes":
        print("\n" * 20)
    else:
        game_over= True
highest_bid = {}
highest_bid_name = "";
highest_bid_amount = 0

for name in bid_data:
    if highest_bid_amount < bid_data[name]:
        highest_bid_name = name
        highest_bid_amount = bid_data[name]
print(f"{highest_bid_name} Won the Auction For {highest_bid_amount} $")

# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


