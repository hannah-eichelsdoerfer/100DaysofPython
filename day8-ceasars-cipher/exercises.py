# Functions with Inputs
def personal_greeting(name):
  print(f"Hello {name} 👋")

personal_greeting("Hannah")
# Positional vs. Keyword Arguments
def greet_with(name, location):
  print(f"Hello {name} 👋")
  print(f"What is it like in {location}? 🌍")

greet_with("Hannah", "Gold Goast")

# Positional Arguments
greet_with("Gold Coast", "Hannah")
# will mess up our desired argument because of something caleld positional argument

# Keyword Arguments
def my_function(a, b, c):
  # do something with a
  # do something with b
  # doe something with c
 print(a + b * c)

my_function(c=3, a=1, b=2)

greet_with(location="Gold Coast", name="Hannah")

# Paint Area Calculator
import math

def paint_calc(height, width, cover):
  number_of_cans = math.ceil((height * width) / cover)
  print(f"You'll need {number_of_cans} cans of paint.")
  
# 🚨 Testing Code 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# Prime Number Checker
# prime number is a number only divisible by 1 or itself
# 2, 3, 5, 7, 11, 13 ...

def prime_checker(number):
  prime_num = True
  
  for i in range(2, number):
    if number % i == 0:
      prime_num = False
  
  if prime_num:
    print(f"{number} is not a prime number")
  else:
    print(f"{number} is a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)