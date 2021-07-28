# Day 9 - Silent Auction Program
from os import system, name
def clear():
  # for windows
  if name == 'nt':
      _ = system('cls')
  # for mac and linux(here, os.name is 'posix')
  else:
      _ = system('clear')
      
from art import logo
clear()
print(logo)
print("Welcome to the secret auction program 💰")

auction = {}
bidding_possible = True

# def highest_bidder(bids):
  # winner_name = ""
  # winning_amount = 0
  # for bidder in auction:
  #   bid_amount = auction[bidder]
  #   if bid_amount > winning_amount:
  #     winning_amount = bid_amount
  #     winner_name = bidder
  # print(f"The winner is {winner_name} with a bid of ${winning_amount}")

while bidding_possible:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  auction[name] = bid
  others = input("Are there any other bidders? Type 'yes' or 'no'. ")
  
  if others == "yes":
    clear()
  elif others == "no":
    bidding_possible = False
    winner_name = ""
    winning_amount = 0
    for bidder in auction:
      bid_amount = auction[bidder]
      if bid_amount > winning_amount:
        winning_amount = bid_amount
        winner_name = bidder
    print(f"👉🏻 The winner is {winner_name} with a bid of ${winning_amount}")
  