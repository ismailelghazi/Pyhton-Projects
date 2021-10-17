import  logo
print(logo)
Add_Person = False
new_name = []

high=0
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")



while True:
    BlindDict = {}
    name = input("give me your name if you want join to this khra ")
    build = float(input("bcja7l dakhl nta asat "))
    BlindDict[name] = bui
    Add_Person = int(input("Do you want to add more users (0 or 1)?\n"))
    if Add_Person ==0:
        find_highest_bidder(BlindDict)
    else:
        break
print(new_name)