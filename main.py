from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
bid_details = {}
flag = "yes"

while flag == "yes":
  name = input("What is your name? ")
  bid = input("What is your bid?: $")
  bid_details[name] = int(bid)
  flag = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
  clear()

#print(bid_details)

# highest_bidder = ""
# highest_bid = 0

# for keys in bid_details:
#   if bid_details[keys] > highest_bid:
#     highest_bidder = keys
#     highest_bid = bid_details[keys]

# print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")





highest_bid = {}
bidMax = 0
for keys in bid_details:
  if bid_details[keys] >= bidMax:
    highest_bid[keys] = bid_details[keys]
    bidMax = bid_details[keys]

for keys in highest_bid:
  print(f"The winner is {keys} with a bid of ${highest_bid[keys]}")