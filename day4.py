# Randomisation and Python Lists
# opposite of deterministic (predictible)
# pseudo random number generatos - Python uses Mersenne Twister

# PYTHON MODULES
# -> code is usually split up into individual modules (to avoid the code getting to long)
# where each modul is module is responsible for a diffrent bit of functionality of the program
# creating own module:
# main.py is entry point, new file on same level my_module.py
# import my_module in main file to use code
# use it with saying my_module.something

# random module (generate random numbers/sequences) - created by Python
import random

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

random_float_between_one_and_five = random.random() * 5
print(random_float_between_one_and_five)

lovescore = random.randint(1, 100)
print(f"Your love score is {lovescore}💓")

# Heads or Tails
heads_tails = random.randint(0, 1)
if heads_tails == 0:
  print("Heads")
else:
  print("Tails")

# Lists (data structure) - way of organizing and storing data in python
states_in_australia = ["Victoria", "New Sout Wales", "South Australia", "Queensland", "Tasmania", "Western Australia", "Nothern Territory"]

# append to add single item at the end
# extend (you can add a whole list of other items in square brackets)
# overview: https://docs.python.org/3/tutorial/datastructures.html

# Banker Roulette - Who will pay the bill?
names_string = input("Write down everybody names, seperated by commas: \n")
names = names_string.split(", ")

random_person = random.randint(0, len(names) - 1)

print(f"➡  {names[random_person]} has to pay the bill 💸")

# Shorter way:
# random_payer = random.choice(names)
# print(random_payer)

# Index Erros and working with Nested Lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]

# Treasure Map
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "✖ "

print(f"{row1}\n{row2}\n{row3}")


# Day 4 Project - Rock Paper Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rock_paper_scissor = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if choice > 2 or choice < 0:
  print("You typed an invalid number, therefore you lost... 🤦🏻‍♀️")
else:
  print(rock_paper_scissor[choice])
  print("Computer chose:")
  computer_choice = random.randint(0, 2)
  print(rock_paper_scissor[computer_choice])

  if choice == computer_choice:
    print("Its a tie, noone wins")
  elif choice == 0 and computer_choice == 2:
    print("You won!!! 🏆")
  elif choice == 2 and computer_choice == 0:
    print("You lost!!! 😢")
  elif choice < computer_choice:
    print("You lost!!! 😢")
  elif choice > computer_choice:
    print("You won!!! 🏆")

# choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")
# if choice == "0":
#   print(rock)
# elif choice == "1":
#   print(paper)
# elif choice == "2":
#   print(scissors)

# print("Computer chose:")
# computer_choice = random.randint(0, 2)
# if computer_choice == 0:
#   print(rock)
# elif computer_choice == 1:
#   print(paper)
# elif computer_choice == 2:
#   print(scissors)