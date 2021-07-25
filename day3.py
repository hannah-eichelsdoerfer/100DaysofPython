# (nested) if-else statements, comparison operators (>, <, <=, >=, ==, !=)
# elif
# Multiple conditions (multiple if statements in succession)
print("Welcome to the rollercoaster 🎢")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("How old are you? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5")
  elif age < 18 :
    bill = 7
    print("Youth tickets are $7")
  elif age >= 45 and age <= 55:
    print("People your age ride for free!")
  else:
    bill = 12
    print("$12 for an adult ticket")
  
  photo = input("Do you want a photo taken? Y/N. ")
  if photo == "Y":
    bill += 3
  print(f"Your final bill is ${bill}")   
else:
  print("Sorry, you have to grow taller before you can ride.")
  
# Odd or Even Exercise (Modulo Operation)
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
  print("This is an even number")
else:
  print("This is an odd number")

# BMI Calculator advanced ⚖
height = float(input("Enter your height in cm: ")) / 100
weight = float(input("Enter your weight in kg: "))

bmi = round((weight / (height * height)), 1)

print(f"Your BMI is {bmi}.");

if bmi < 18.5:
  print("You are underweight")
elif bmi < 25:
  print("You have a normal weight")
elif bmi < 30:
  print("You are overweight")
elif bmi < 35:
  print("You are obwese")
else:
  print("You are clinically obese")
  
# Leap Year
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap Year!")
    else:
      print("Not a leap year!")
  else:
    print("Leap year!")
else:
  print("Not a leap year!")
  
# Pizza Order Program 🍕
# Logical operators (written out in python)
# and (equivalent to writing &&)
# or (equivalent of ||)
# not

print("Welcome to Python Pizza Deliveries!")
size = input("What size do you want your pizza? S, M or L? ")
add_pepperoni = input("Do you want pepperoni? ")
cheesy_crust = input("Do you want a cheesy crust? ")

price = 0

if size == "S":
  price += 15
elif size == "M":
  price += 20
elif size == "L":
  price += 25

if add_pepperoni == "Y" and size == "S":
  price += 2
else:
  price += 3
  
if cheesy_crust == "Y":
  price += 1
  
print(f"Your final bill is ${price}💵")

# Love Calculator
# lower() function changes all the letters in a string to lowercase
# count() function will give you the number of times a letter occurs in a string
print("Welcome to the Love Calculator 💕")
name1 = input("Whats your name? \n").lower()
name2 = input("Whats your lovers name? \n").lower()

lovescore = 0

firstNumber = 0
firstNumber += name1.count("t")
firstNumber += name1.count("r")
firstNumber += name1.count("u")
firstNumber += name1.count("e")
firstNumber += name2.count("t")
firstNumber += name2.count("r")
firstNumber += name2.count("u")
firstNumber += name2.count("e")

# print(name1, name2, firstNumber)

secondNumber = 0
secondNumber += name1.count("l")
secondNumber += name1.count("o")
secondNumber += name1.count("v")
secondNumber += name1.count("e")
secondNumber += name2.count("l")
secondNumber += name2.count("o")
secondNumber += name2.count("v")
secondNumber += name2.count("e")

lovescore = int(str(firstNumber) + str(secondNumber))

if lovescore < 10 or lovescore > 90:
  print(f"Your score is {lovescore}, you to together like coke and mentos")
elif lovescore >= 40 and lovescore <= 50:
  print(f"Your score is {lovescore}, you are alright together")
else:
  print(f"Your score is {lovescore}")
  
# Day 3 Project - Treasue Island
print('''
______________________________________________________________
           _  _             _  _
  .       /\\/%\       .   /%\/%\     .
      __.<\\%#//\,_       <%%#/%%\,__  .
.    <%#/|\\%%%#///\    /^%#%%\///%#\\
      ""/%/""\ \""//|   |/""'/ /\//"//'
 .     L/'`   \ \  `    "   / /  ```
        `      \ \     .   / /       .
 .       .      \ \       / /  .
        .        \ \     / /          .
   .      .    ..:\ \:::/ /:.     .     .
______________/ \__;\___/\;_/\________________________________
''')
print("Welcome to Treasue Island 🏴‍☠️")
print("Your missure is to find the treasure...")

direction = input("--- You are at a crossroad, where do you want to go? Type 'left' or 'right': \n").lower()
if direction == "right":
  print("Game over, you fell into a well hidden trap.")
elif direction == "left":
  action = input("--- You've reached the shore of the ocean but you see an island in the middle. Type 'wait' to wait for a boat or 'swim' to make the journey across yourself.\n").lower()
  if action == "swim":
    print("Game over, you were eaten by a crocodile while swimming towards the island 🐊")
  elif action == "wait":
    door = input("--- You arrived at the island unharmed, there are three hidden doors in the sand, a red, a yellow and a blue one. Which color do you choose? \n").lower()
    if door == "red":
      print("Game over - huge flames shot out of the door 🔥")
    elif door == "yellow":
      print("You found the treasure - you won!!! 🏆")
    elif door == "blue":
      print("The blue door let the water flood the island, you've drowned 🌊")
    else:
      print("Game over. You starved looking for a door with this color.")
    